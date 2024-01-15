from peewee import Model, CharField, FloatField, BooleanField, TextField

from camosam_backend.models.config import database


class BaseModel(Model):
    class Meta:
        database = database


class Guest(BaseModel):
    name = CharField()
    email = CharField()
    phone = CharField()
