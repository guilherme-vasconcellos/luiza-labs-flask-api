import pytest

from server import create_app

from sqlalchemy import create_engine

endpoint = 'http://localhost:5000/employee'


@pytest.fixture(scope='session')
def app():
    app = create_app('app/config.py')
    app.testing = True

    return app


@pytest.fixture(scope='session')
def conn(app):
    engine = create_engine(app.config.get('SQLALCHEMY_DATABASE_URI'))
    return engine


@pytest.fixture(scope='function')
def clear(conn):
    conn.execute('DELETE from Employee')

    yield

    conn.execute('DELETE from Employee')


@pytest.fixture(scope='function')
def seed(app):
    employees = [{'name': 'John Doe 1',
                  'email': 'johndoe1@test.com',
                  'department': 'TI 1'},
                 {'name': 'John Doe 2',
                  'email': 'johndoe2@test.com',
                  'department': 'TI 2'},
                 {'name': 'John Doe 3',
                  'email': 'johndoe3@test.com',
                  'department': 'TI 3'}]

    with app.test_client() as client:
        for employee in employees:
            client.post(endpoint, json=employee)


def test_create_an_employee_with_success(app, clear):
    with app.test_client() as client:
        employee = {'name': 'John Doe',
                    'email': 'johndoe@test.com',
                    'department': 'TI'}

        expected_response = {'id': 'e0c50c8a-787e-43c7-9acd-08cf589d551e',
                             'name': 'John Doe',
                             'email': 'johndoe@test.com',
                             'department': 'TI',
                             'createdAt': '2019-07-22T22:08:21.196Z',
                             'updatedAt': '2019-07-22T22:08:21.196Z'}

        response = client.post(endpoint, json=employee)

        assert response.status_code == 201

        assert response.json.get('id') is not None
        assert response.json.get('createdAt') is not None
        assert response.json.get('updatedAt') is not None


def test_return_error_when_try_to_create_an_employee_without_required_fields(app):
    with app.test_client() as client:
        employee = {'name': 'John Doe',
                    'email': 'johndoe@test.com'}

        response = client.post(endpoint, json=employee)

        assert response.status_code == 400
        assert 'Employee department is required' in response.json.get('error')


def test_return_list_of_employees(app, clear, seed):
    with app.test_client() as client:
        response = client.get(endpoint)

        assert response.status_code == 200
        assert len(response.json) == 3


def test_return_one_employee(app, seed, clear):
    with app.test_client() as client:
        email = 'johndoe1@test.com'
        response = client.get(f'{endpoint}/{email}')

        assert response.status_code == 200
        assert response.json.get('email') == email


def test_return_error_when_try_to_find_inexistent_employee(app, clear):
    with app.test_client() as client:
        email = 'johndoe@test.notexists.com'
        response = client.get(f'{endpoint}/{email}')

        assert response.status_code == 404
        assert f'Employee with email: "{email}" not found' in response.json.get(
            'error')


def test_update_employee_with_success(app, clear, seed):
    with app.test_client() as client:
        email = 'johndoe1@test.com'
        update = {'name': 'John Doe Harisson'}

        response = client.put(f'{endpoint}/{email}', json=update)

        assert response.status_code == 200
        assert response.json.get('email') == email
        assert response.json.get('name') == 'John Doe Harisson'


def test_return_error_when_try_to_updated_inexistent_employee(app, clear):
    with app.test_client() as client:
        email = 'johndoe@test..notexists.com'
        update = {'name': 'John Doe Harisson'}

        response = client.put(f'{endpoint}/{email}', json=update)

        assert response.status_code == 404
        assert f'Employee with email: "{email}" not found' in response.json.get(
            'error')


def test_delete_employee_with_success(app, seed):
    with app.test_client() as client:
        email = 'johndoe1@test.com'
        response = client.delete(f'{endpoint}/{email}')

        assert response.status_code == 204


def test_return_error_when_try_delete_inexistent_employee(app, clear):
    with app.test_client() as client:
        email = 'johndoe@test.notexists.com'
        response = client.delete(f'{endpoint}/{email}')

        assert response.status_code == 404
        assert f'Employee with email: "{email}" not found' in response.json.get(
            'error')
