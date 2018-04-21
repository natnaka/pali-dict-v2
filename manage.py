import os
from flask_script import Manager, Shell
from application import create_app
from application.models import db
import application.models as models

app = create_app()
manager = Manager(app)

def _make_shell_context():
    d = {}
    d['app'] = app
    d['db'] = db
    d['m'] = models
    return d

manager.add_command('shell', Shell(make_context=_make_shell_context))

@manager.option("--port", "-p", dest="port", default=5000)
@manager.option("--host", "-h", dest="bind", default='0.0.0.0')
def run(port, bind):
    """Run app"""
    app.run(port=port, host=bind)

@manager.command
def create_db():
    db.create_all()

@manager.command
def drop_db():
    db.drop_all()

if __name__ == '__main__':
    manager.run()
