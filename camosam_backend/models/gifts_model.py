from peewee import Model, CharField, FloatField, BooleanField, TextField

from camosam_backend.models.config import database


class BaseModel(Model):
    class Meta:
        database = database


class Gift(BaseModel):
    name = CharField()
    image_url = TextField()
    price = FloatField()
    is_active = BooleanField()


# database.connect()
# database.create_tables([Gift])
# database.close()
