from application.extensions import db
from datetime import datetime

 
class Following(db.Model):
    __tablename__ = 'followings'
    id = db.Column(db.Integer,primary_key=True)
    followed_by = db.Column(db.Integer)
    user_id = db.Column(db.Integer,db.ForeignKey('users.id'))









