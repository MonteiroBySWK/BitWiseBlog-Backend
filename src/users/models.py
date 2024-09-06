from sqlalchemy import Column, Integer, Text
from ..app import db


class UserModel(db.Model):
    __tablename__: str = "users"

    id = Column(Integer, primary_key=True, autoincrement=True)
    username = Column(Text, nullable=False, unique=True)
    email = Column(Text, nullable=False, unique=True)
    password = Column(Text, nullable=False)

    def __repr__(self) -> str:
        return f"Account(id={self.id}, username={self.username}, email={self.email})"

    def __str__(self):
        return f"Account: {self.username}"
