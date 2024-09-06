from DBConnectionHandler import DBConnectionHandler
from .models import PostModel


class PostRepository:
    def select_all(self):
        with DBConnectionHandler() as db:
            if db.session is not None:
                data = db.session.query(PostModel).all()
                return data
            else:
                return []

    def select_by_id(self, id: int):
        with DBConnectionHandler() as db:
            if db.session is not None:
                data = db.session.query(PostModel).filter(PostModel.id == id).all()
                return data
            else:
                return []

    def select_by_condition(self, condition):
        with DBConnectionHandler() as db:
            if db.session is not None:
                data = db.session.query(PostModel).filter(condition).all()
                return data
            else:
                return []

    def insert(self, title: str, author: str, contain: str):
        with DBConnectionHandler() as db:
            if db.session is not None:
                new_post = PostModel(title=title, author=author, contain=contain)
                db.session.add(new_post)
                db.session.commit()

    def delete(self, id: int):
        with DBConnectionHandler() as db:
            if db.session is not None:
                db.session.query(PostModel).filter(PostModel.id == id).delete()

    def update(
        self,
        id: int,
        title: str | None = None,
        author: str | None = None,
        contain: str | None = None,
    ):
        with DBConnectionHandler() as db:
            if db.session is not None:
                data_updated = {}
                if title is not None:
                    data_updated["title"] = title
                if author is not None:
                    data_updated["author"] = author
                if contain is not None:
                    data_updated["contain"] = contain

                db.session.query(PostModel).filter(PostModel.id == id).update(
                    data_updated
                )


if __name__ == "__main__":
    db = PostRepository()
    print(db.select_all())
