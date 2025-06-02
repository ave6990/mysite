from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField

class ConditionsFilter(FlaskForm):
  date_from = StringField('Дата от')
  date_to = StringField('Дата до')
  location = StringField('Место')
  comment = StringField('Комментарий')
  submit = SubmitField('Фильтровать')
