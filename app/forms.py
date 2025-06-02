from flask_wtf import FlaskForm
from wtforms import SelectField, StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import DataRequired

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
