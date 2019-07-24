import json

from flask import current_app as app, Blueprint, request, jsonify

from app.repositories.employee_repository import EmployeeRepository

employee_bp = Blueprint('employee', __name__)


@employee_bp.route('/', methods=['POST'])
def create():
    payload = request.get_data()
    payload = json.loads(payload)

    try:
        created = EmployeeRepository.create(payload)

        return jsonify(created), 201
    except Exception as e:
        error = {'error': str(e)}
        return jsonify(error), 400


@employee_bp.route('/', methods=['GET'])
def all():
    try:
        employees = EmployeeRepository.all()
        return jsonify(employees), 200
    except Exception as e:
        error = {'error': str(e)}
        return jsonify(error), 400


@employee_bp.route('/<string:email>', methods=['GET'])
def find_by_email(email):
    try:
        employee = EmployeeRepository.find_by_email(email)
        return jsonify(employee), 200
    except Exception as e:
        error = {'error': str(e)}
        return jsonify(error), 404


@employee_bp.route('/<string:email>', methods=['PUT'])
def update_by_email(email):
    payload = request.get_data()
    payload = json.loads(payload)

    try:
        employee = EmployeeRepository.update_by_email(email, payload)
        return jsonify(employee), 200
    except Exception as e:
        error = {'error': str(e)}
        return jsonify(error), 404


@employee_bp.route('/<string:email>', methods=['DELETE'])
def delete_by_email(email):
    payload = request.get_data()
    payload = json.loads(payload)

    try:
        employee = EmployeeRepository.delete_by_email(email)
        return jsonify(employee), 204
    except Exception as e:
        error = {'error': str(e)}
        return jsonify(error), 404
