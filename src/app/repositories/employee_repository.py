from app.models.employee import Employee


class EmployeeRepository(object):
    @classmethod
    def create(cls, payload):
        """
        @author Guilherme Vasconcellos <guiyllw@hotmail.com>
        @description Method to create an employee from json object

        @param employee Object containing employee data to create
        """
        employee = Employee(**payload)
        employee.create()

        return Employee.as_dict(employee)

    @classmethod
    def all(cls):
        """
        @author Guilherme Vasconcellos <guiyllw@hotmail.com>
        @description Method to list employees by filter
        """
        employees = Employee.query.all()

        return Employee.as_list(employees)

    @classmethod
    def find_by_email(cls, email):
        """
        @author Guilherme Vasconcellos <guiyllw@hotmail.com>
        @description Method to get an employee by email

        @param email Employee email to find on database
        """
        employee = Employee.query.filter_by(email=email).first()
        if not employee:
            raise ValueError(f'Employee with email: "{email}" not found')

        return Employee.as_dict(employee)

    @classmethod
    def update_by_email(cls, email, new_employee):
        """
        @author Guilherme Vasconcellos <guiyllw@hotmail.com>
        @description Method to update an employee by email

        @param email Employee email to update on database
        @param new_employee Partial employee data to update on database
        """
        updated = Employee.update(email, new_employee)
        if not updated:
            raise ValueError(f'Employee with email: "{email}" not found')

        employee = Employee.query.filter_by(email=email).first()

        return Employee.as_dict(employee)

    @classmethod
    def delete_by_email(cls, email):
        """
        @author Guilherme Vasconcellos <guiyllw@hotmail.com>
        @description Method to delete an employee by email

        @param email Employee email to delete on database
        """
        employee = Employee.query.filter_by(email=email).first()
        if not employee:
            raise ValueError(f'Employee with email: "{email}" not found')

        employee.delete()
