#!/usr/bin/env python
# encoding: utf-8

from flask_script import Manager, Shell, Option,Command
from app import create_app
#from gunicornserver  import GunicornServer
app = create_app('development')
manager = Manager(app)

@manager.option('-h', '--host', dest='host', default='0.0.0.0')
@manager.option('-p', '--port', dest='port', type=int, default=5000)
@manager.option('-w', '--workers', dest='workers', type=int, default=3)
def gunicorn(host, port, workers):
    """Start the Server with Gunicorn"""
    from gunicorn.app.base import Application

    class FlaskApplication(Application):
        def init(self, parser, opts, args):
            return {
                'bind': '{0}:{1}'.format(host, port),
                'workers': workers
            }

        def load(self):
            return app

    application = FlaskApplication()
    return application.run()


#manager.add_command("gunicorn", GunicornServer())

if __name__ == '__main__':
    manager.run()

