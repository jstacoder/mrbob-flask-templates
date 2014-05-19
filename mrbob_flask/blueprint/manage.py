from flask.ext.script import Server,Shell,Manager,prompt_bool
from {{ app.name }} import db, app, models

manager = Manager(app)

@manager.command
def syncdb():
    if prompt_bool('Are you sure, this will delete your database'):
        db.drop_all()
        db.create_all()
    else:
        pass

def _make_context():
    ctx = {}
    ctx['db'] = db
    ctx['app'] = app
    ctx['models'] = models
    return ctx


manager.add_command("shell",Shell(make_context=_make_context))
manager.add_command("runserver",Server(host='0.0.0.0',port=8080,debug=True))

manager.run()
