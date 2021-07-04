from flask import Flask
from config import Configuration
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

""" Master blueprint file """

def create_app():
    app = Flask(__name__)
    app.config.from_object(Configuration)

    from admin.admin import admin
    from frontend.frontend import frontend

    app.register_blueprint(admin, url_prefix='/admin')
    app.register_blueprint(frontend, url_prefix='/')

    return app


app = create_app()
db = SQLAlchemy(app)
migrate = Migrate(app, db)

from models import Post, Tag
