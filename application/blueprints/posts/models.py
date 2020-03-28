
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
    
    def unfollow(self, user):
        f = self.followed.filter_by(followed_id=user.id).first()
        if f:
            db.session.delete(f)

    def is_following(self, user):
        if user.id is None:
            return False
        return self.followed.filter_by(
            followed_id=user.id).first() is not None

    def is_followed_by(self, user):
        if user.id is None:
            return False
        return self.followers.filter_by(
            follower_id=user.id).first() is not None
