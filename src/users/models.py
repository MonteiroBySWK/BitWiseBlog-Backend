from sqlalchemy.schema import Column
from sqlalchemy.types import String


class UserModel:
    __tablename__: str = "users"

    id = Column()
    username = Column(String)
    email = Column(String)
    password = Column(String)

    def __str__(self):
        return f"Account: {self.username}"
