# -*- coding: utf-8 -*-


from flask_script import Manager

from bookhouse.main import create_app_main

app = create_app_main()


manager = Manager(app)


@manager.command
def create():
    from bookhouse.core import db

    db.create_all()


if __name__ == '__main__':
    manager.run()
