from peewee import Model, CharField, FloatField, BooleanField

from .config import database


class BaseModel(Model):
    class Meta:
        database = database


class Gifts(BaseModel):
    name = CharField()
    image_url = CharField()
    price = FloatField()
    is_active = BooleanField()


# database.connect()
# database.create_tables([Gifts])
# database.close()
