from flask import Flask , render_template,request,redirect,url_for
from models import db_setup,Course
from flask_migrate import Migrate


application=Flask(__name__)
db_setup(application,Migrate)

@application.route('/')
def home():
    courses=Course.query.all()
    return render_template('index.html',courses=courses)

@application.route('/new_course',methods=['POST'])
def new_course():
    name=request.form.get('name')
    newTopic=Course(name=name)
    newTopic.commit()
    return redirect(url_for('home'))

if __name__=='__main__':
    application.run()