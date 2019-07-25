from uuid import uuid4

from app.models.base import db, ma, ModelMixin


class Employee(db.Model, ModelMixin):
    """
    @author: Guilherme Vasconcellos <guiyllw@hotmail.com>
    """
    __tablename__ = 'Employee'

    id = db.Column('id', db.String(100), primary_key=True)
    name = db.Column('name', db.String(100), nullable=False)
    email = db.Column('email', db.String(100), nullable=False, unique=True)
    department = db.Column('department', db.String(100), nullable=False)

    def __init__(self, **employee):
        self.id = str(uuid4())

        if not 'name' in employee:
            raise ValueError('Employee name is required')

        if not 'email' in employee:
            raise ValueError('Employee email is required')

        if not 'department' in employee:
            raise ValueError('Employee department is required')

        self.name = employee.get('name')
        self.email = employee.get('email')
        self.department = employee.get('department')

    def create(self):
        created = db.session.add(self)
        db.session.commit()

        return created

    def delete(self):
        deleted = db.session.delete(self)
        db.session.commit()

        return deleted

    @classmethod
    def update(cls, email, employee):
        if 'createdAt' in employee:
            del employee['createdAt']

        if 'updatedAt' in employee:
            del employee['updatedAt']

        updated = cls.query.filter_by(email=email).update(employee)
        db.session.commit()

        return updated


class EmployeeSchema(ma.ModelSchema):
    class Meta:
        model = Employee
