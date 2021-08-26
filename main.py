from flask import Flask
from flask_session import Session

from config.data_source import DATABASE_URL, SECRET_KEY, db
from controller.auth_controller import auth_url

from controller.guruh_controller import guruh_url
from controller.talaba_controller import talaba_url
from controller.yunalish_controller import yunalish_url
from model.user import User
from public_urls import public_url
from flask_login import LoginManager

app = Flask(__name__)

app.register_blueprint(public_url)
app.register_blueprint(yunalish_url)
app.register_blueprint(guruh_url)
app.register_blueprint(talaba_url)
app.register_blueprint(auth_url)


app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
app.config['SQLALCHEMY_DATABASE_URI'] = DATABASE_URL
app.config['SECRET_KEY'] = SECRET_KEY
db.init_app(app)
app.app_context().push()
db.create_all()
SESSION_TYPE = 'filesystem'
app.config.from_object(__name__)
Session(app)





login_manager = LoginManager()
login_manager.init_app(app)
@login_manager.user_loader
def load_user(user_id):
    return User.get(user_id)



if __name__ == "__main__":
    app.run(debug=True)
