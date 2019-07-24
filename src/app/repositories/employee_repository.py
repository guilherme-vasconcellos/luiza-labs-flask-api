from app.models.employee import Employee


class EmployeeRepository(object):
    @classmethod
    def create(cls, payload):
        employee = Employee(**payload)
        employee.create()

        return Employee.as_dict(employee)

    @classmethod
    def all(cls):
        employees = Employee.query.all()

        return Employee.as_list(employees)

    @classmethod
    def find_by_email(cls, email):
        employee = Employee.query.filter_by(email=email).first()
        if not employee:
            raise ValueError(f'Employee with email: "{email}" not found')

        return Employee.as_dict(employee)

    @classmethod
    def update_by_email(cls, email, update):
        updated = Employee.update(email, update)
        if not updated:
            raise ValueError(f'Employee with email: "{email}" not found')

        employee = Employee.query.filter_by(email=email).first()

        return Employee.as_dict(employee)

    @classmethod
    def delete_by_email(cls, email):
        employee = Employee.query.filter_by(email=email).first()
        if not employee:
            raise ValueError(f'Employee with email: "{email}" not found')

        employee.delete()
