from datetime import datetime
from itsdangerous import TimedJSONWebSignatureSerializer as Serializer
from flask import current_app
from flaskblog import db, login_manager
from flask_login import UserMixin

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    image_file = db.Column(db.String(20), nullable=False, default='default.jpg')
    password = db.Column(db.String(60), nullable=False)
    posts = db.relationship('Post', backref='author', lazy=True)

    def get_reset_token(self, expires_sec=1800):
        s = Serializer(current_app.config['SECRET_KEY'], expires_sec)
        return s.dumps({'user_id': self.id}).decode('utf-8')

    @staticmethod
    def verify_reset_token(token):
        s = Serializer(current_app.config['SECRET_KEY'])
        try:
            user_id = s.loads(token)['user_id']
        except:
            return None
        return User.query.get(user_id)

    def __repr__(self):
        return f"User('{self.username}', '{self.email}', '{self.image_file}')"


class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    date_posted = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    content = db.Column(db.Text, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

    def __repr__(self):
        return f"Post('{self.title}', '{self.date_posted}')"

class Follow(db.Model): 
	_tablename_ = 'follows' 
	follower_id = db.Column(db.Integer, db.ForeignKey('users.id'), primary_key=True) 
	followed_id = db.Column(db.Integer, db.ForeignKey('users.id'), primary_key=True) 
	timestamp = db.Column(db.DateTime, default=datetime.utcnow)

def follow(self, user):
        if not self.is_following(user):
            f = Follow(follower=self, followed=user)
        db.session.add(f)

def unfollow(self, user):
    f = self.followed.filter_by(followed_id=user.id).first()
    if f:
        db.session.delete(f)

def is_following(self, user):
    return self.followed.filter_by(
        followed_id=user.id).first() is not None

def is_followed_by(self, user):
    return self.followers.filter_by(
        follower_id=user.id).first() is not None