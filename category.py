import datetime
import sqlalchemy
from sqlalchemy import orm

from .db_session import SqlAlchemyBase


class Category(SqlAlchemyBase):
    __tablename__ = 'category'

    title = sqlalchemy.Column(sqlalchemy.String, nullable=True, primary_key=True)
