from sqlalchemy import Column, Integer, Text
from ..app import db


class PostModel(db.Model):
    __tablename__ = "posts"

    id = Column(Integer, primary_key=True, autoincrement=True, unique=True)
    title = Column(Text, nullable=False, unique=True)
    author = Column(Text, nullable=False)
    contain = Column(Text, nullable=False)
    likes = Column(Integer, insert_default=0)
    dislikes = Column(Integer, insert_default=0)

    def __init__(self, title, author, contain):
        super().__init__()
        self.title = title
        self.author = author
        self.contain = contain

    def __repr__(self) -> str:
        return f"Post(id={self.id},author={self.author}, 'title={self.title}', likes={self.likes}, dislikes={self.dislikes})"

    def __str__(self) -> str:
        return f"Post by {self.author}"
