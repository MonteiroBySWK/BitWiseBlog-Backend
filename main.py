import os
from src.app import create_app

flask_app = create_app()


if __name__ == "__main__":
    os.system("flask --app main run --debug")
