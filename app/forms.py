from flask_wtf import FlaskForm
from wtforms import SelectField, StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import DataRequired

class LoginForm(FlaskForm):
  #username = StringField('Имя пользователя', validators = [DataRequired()])
  username = SelectField('Пользователь', choices=[], validators = [DataRequired()])
  password = PasswordField('Пароль', validators = [DataRequired()])
  #remember_me = BooleanField('Запомнить меня')
  submit = SubmitField('Войти')

class ConditionsFilter(FlaskForm):
  date_from = StringField('Дата от')
  date_to = StringField('Дата до')
  location = StringField('Место')
  comment = StringField('Комментарий')
  submit = SubmitField('Фильтровать')

class VerificationsFilter(FlaskForm):
  upload = BooleanField('Выгружено')
  count = StringField('Счет')
  engineer = StringField('Поверитель')
  date = StringField('Дата')
  mi_type = StringField('Тип СИ')
  components = StringField('Состав')
  serial_number = StringField('Зав. №')
  registry_number = StringField('Рег. №')
  counteragent = StringField('Собственник')
