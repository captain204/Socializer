from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash
from application.extensions import db
from datetime import datetime
from application.blueprints.follows.models import(
     Follow) 



class User(UserMixin, db.Model):
    """User Model """

    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), unique=True, nullable=False)
    firstname = db.Column(db.String(100), nullable=False)
    lastname = db.Column(db.String(100), nullable=False)
    password = db.Column(db.String(250), unique=True, nullable=False)
    posts = db.relationship('Post', backref=db.backref('posts',lazy=True))
    followed = db.relationship('Follow',
                               foreign_keys=[Follow.follower_id],
                               backref=db.backref('follower', lazy='joined'),
                               lazy='dynamic',
                               cascade='all, delete-orphan')
    followers = db.relationship('Follow',
                              foreign_keys=[Follow.followed_id],
                              backref=db.backref('followed', lazy='joined'),
                              lazy='dynamic',
                              cascade='all, delete-orphan')
    created_on = db.Column(db.DateTime,default=datetime.utcnow)
    

    def set_password(self,password):
        """Create User Password """
        self.password = generate_password_hash(password,method='sha256')

    def check_password(self,password):
        """Check Hashed Password"""
        return check_password_hash(self.password,password)

    def is_following(self, user):
        if user.id is None:
            return False
        return self.followed.filter_by(followed_id=user.id).first() is not None

    def is_followed_by(self, user):
        if user.id is None:
            return False
        return self.followers.filter_by(
            follower_id=user.id).first() is not None
    
    def follow(self, user):
       if not self.is_following(user):
            f = Follow(follower=self, followed=user)
            db.session.add(f) 


    def unfollow(self, user):
        f = self.followed.filter_by(followed_id=user.id).first()
        if f:
            f = self.followed.filter_by(followed_id=user.id).first()
            db.session.delete(f)
            return True
    




    def __repr__(self):
        return '<User {}>'.format(self.username)
