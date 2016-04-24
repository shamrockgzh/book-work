# -*- coding: utf-8 -*-

from flask import Flask
from flask_sqlalchemy import SQLAlchemy


def create_app_main():
    app = Flask(__name__)
    app.config.from_object('bookhouse.main.config')
    db = SQLAlchemy()

    import bookhouse.core
    bookhouse.core.app = app
    bookhouse.core.db = db

    db.init_app(app)

    import bookhouse.models.user
    import bookhouse.models.book

    import bookhouse.main.views
    import bookhouse.main.views.user
    import bookhouse.main.views.book

    return app
