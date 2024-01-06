import os

from dotenv import load_dotenv
from peewee import PostgresqlDatabase

load_dotenv(override=True)

database = PostgresqlDatabase(
    os.getenv('DATABASE_NAME'),
    user=os.getenv('DATABASE_USER'),
    password=os.getenv('DATABASE_PASSWORD'),
    port=os.getenv('DATABASE_PORT'),
    host=os.getenv('DATABASE_HOST'),
)
