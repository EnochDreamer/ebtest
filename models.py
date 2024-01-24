from flask_sqlalchemy import SQLAlchemy
import os
from dotenv import load_dotenv

load_dotenv()
if 'RDS_HOSTNAME' in os.environ:
    db_host=os.environ.get('RDS_HOSTNAME')
    db_port=os.environ.get('RDS_PORT')
    db_name=os.environ.get('RDS_DB_NAME')
    db_username=os.environ.get('RDS_USERNAME')
    db_password=os.environ.get('RDS_PASSWORD')
    database_path=f'postgresql://{db_username}:{db_password}@{db_host}:{db_port}/{db_name}'

db=SQLAlchemy()
def db_setup(app,Migrate,database_path=database_path,db=db):
    app.config["SQLALCHEMY_DATABASE_URI"] = database_path
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    app.config["SECRET_KEY"]="hello world"
    db.app = app
    db.init_app(app)
    migrate=Migrate(app,db)
    return app

class Course(db.Model):
    __tablename__='course'
    id=db.Column(db.Integer, primary_key=True)
    name=db.Column(db.String(), nullable=False)
    price=db.Column(db.String,default="$100")
    def commit(self):
        db.session.add(self)
        db.session.commit()
    def delete(self):
        db.session.delete(self)
        db.session.commit()
    def rollback(self):
        db.session.rollback()
    def format(self):
        return {
            "id":self.id,
            "name":self.name,
            "price":self.price
        }