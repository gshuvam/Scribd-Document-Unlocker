from flask_login import UserMixin
from package import db, login_manager


@login_manager.user_loader
def load_user(user_email):
    return User.query.get(str(user_email))

class User(db.Model, UserMixin):
    email = db.Column(db.String(30), unique=True, primary_key = True)
    password = db.Column(db.String(50), nullable = False)
    name = db.Column(db.String(30), nullable=False)

    def get_id(self):
        return (self.email)
