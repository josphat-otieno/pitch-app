from app import create_app, db
from flask_script import Manager, Server
from flask_migrate import Migrate, MigrateCommand
from app.models import User, Pitch, Comments,PitchCategory

# creating the app instance
app = create_app('production')

migrate=Migrate(app,db)
manager = Manager(app)
manager.add_command('server',Server)
manager.add_command('db',MigrateCommand)


@manager.command
def test():
    '''
    Run the unit tests.
    '''
    import unittest
    tests = unittest.TestLoader().discover('tests')
    unittest.TextTestRunner(verbosity=2).run(tests)


# creating python shell
@manager.shell
def make_shell_context():
    return dict(app = app, db = db, User = User, Pitch = Pitch, Comments =Comments, PitchCategory=PitchCategory)


if __name__=='__main__':
    manager.run()
