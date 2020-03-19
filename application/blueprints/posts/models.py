
from application.extensions import db
from datetime import datetime
from application.blueprints.users.models import(
     User) 

    

class Post(db.Model):
    __tablename__ = 'posts'
    id = db.Column(db.Integer, primary_key=True)
    body = db.Column(db.String(256), nullable=False)
    user_id = db.Column(db.Integer,db.ForeignKey('users.id'))
    created_on = db.Column(db.DateTime,default=datetime.utcnow)