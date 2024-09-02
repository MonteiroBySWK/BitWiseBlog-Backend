from ..app import db


class UserModel(db.Model):
    __tablename__: str = "users"

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String)
    email = db.Column(db.String)
    password = db.Column(db.String)

    def __str__(self):
        return f"Account: {self.username}"
