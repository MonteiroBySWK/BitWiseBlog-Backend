import os
from flask import Flask
from src.posts import posts
from src.users import users

app = Flask(__name__)
app.register_blueprint(posts)
app.register_blueprint(users)

if __name__ == "__main__":
    os.system("flask --app main run --debug")
