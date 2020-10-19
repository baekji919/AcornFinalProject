from flask_wtf import FlaskForm
from models import Fcuser
from wtforms import StringField, PasswordField
from wtforms.validators import DataRequired, EqualTo

class RegisterForm(FlaskForm):
    useremail = StringField('useremail', validators=[DataRequired()])
    username = StringField('username', validators=[DataRequired()])
    password = PasswordField('password', validators=[DataRequired(), EqualTo('re_password')])
    re_password = PasswordField('re_password', validators=[DataRequired()])

class LoginForm(FlaskForm):
    class UserPassword(object):
        def __init__(self, message=None):
            self.message = message

        def __call__(self, form, field):
            useremail = form['useremail'].data
            password = field.data
            fcuser = Fcuser.query.filter_by(useremail=useremail).first()
            if fcuser.password != password:
                raise ValueError('정확히 입력해주세요.')

    useremail = StringField('useremail', validators=[DataRequired()])
    password = PasswordField('password', validators=[DataRequired(), UserPassword()])