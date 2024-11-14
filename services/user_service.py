from utils.db import bcrypt
from models.user import User
from utils.db import db

def register_user(username, email, password):
    password_hash = bcrypt.generate_password_hash(password).decode('utf-8')
    new_user = User(username=username, email=email, password_hash=password_hash)
    db.session.add(new_user)
    db.session.commit()
    return new_user

def authenticate_user(username, password):
    user = User.query.filter_by(username=username).first()
    if user and user.check_password(password, bcrypt):
        return user
    return None

def get_user_profile(user_id):
    return User.query.get(user_id)

