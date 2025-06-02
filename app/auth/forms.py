from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired

class LoginForm(FlaskForm):
  username = StringField('Имя пользователя', validators = [DataRequired()])
  #username = SelectField('Пользователь', choices=[], validators = [DataRequired()])
  password = PasswordField('Пароль', validators = [DataRequired()])
  #remember_me = BooleanField('Запомнить меня')
  submit = SubmitField('Войти')


