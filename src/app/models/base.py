from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow

from sqlalchemy.sql import func

from app import models


db = SQLAlchemy()
ma = Marshmallow()


def serializer(instance_type, schema=None, many=False):
    """
    @author: Guilherme Vasconcellos <guiyllw@hotmail.com>
    @description:
        Function to serialize to dict any SQLAlchemy Model based on Schema or native types
    """
    if schema is None:
        return instance_type

    class_type = getattr(models, f'{schema}Schema')

    model_schema = class_type(many=many)
    data_dict = model_schema.dump(instance_type).data

    return data_dict


class ModelMixin(object):
    """
    @author: Guilherme Vasconcellos <guiyllw@hotmail.com>
    @description: Class mixin to SQLAlchemy models
    """
    createdAt = db.Column('createdAt',
                          db.DateTime(timezone=True), default=func.now())
    updatedAt = db.Column('updatedAt',
                          db.DateTime(timezone=True), default=func.now(), onupdate=func.now())

    @classmethod
    def as_dict(cls, result):
        return serializer(result, many=False, schema=cls.__name__)

    @classmethod
    def as_list(cls, results):
        return serializer(results, many=True, schema=cls.__name__)
