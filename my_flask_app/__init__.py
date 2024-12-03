from flask import Flask
from config import Config
from my_flask_app.models import db
from my_flask_app.routes import main


def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    db.init_app(app)

    with app.app_context():
        db.create_all()  # Создание всех таблиц

    app.register_blueprint(main)

    return app

if __name__ == '__main__':
    app = create_app()
    app.run(debug=True)