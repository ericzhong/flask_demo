import os

from flask import url_for, render_template
from flask.ext import admin
from flask.ext.script import Manager

from models.base import db
from models.user import User
from views.login.view import MyModelView, MyAdminIndexView
from application import create_app


app = create_app(__name__)
manager = Manager(app)

admin = admin.Admin(app, 'Auth', index_view=MyAdminIndexView(), base_template='my_master.html')
admin.add_view(MyModelView(User, db.session))


# Flask views
@app.route('/')
def index():
    return render_template('index.html')



@manager.command
def runserver():
    app.run()


@manager.command
def initdb():
    db.drop_all()
    db.create_all()
    
    test_user = User(login="test", password="test",
                     first_name="xxx", last_name="xxx", email="xxx@xxx.com")
    db.session.add(test_user)
    db.session.commit()
    return


if __name__ == "__main__":
    manager.run()