from flask_wtf import FlaskForm
from wtforms import IntegerField, StringField, DateField, SubmitField, validators

class ConditionsFilter(FlaskForm):
  page = IntegerField('Страница', [validators.NumberRange(min=1)], default=1)
  date_from = DateField('Дата от')
  date_to = DateField('Дата до')
  location = StringField('Место')
  comment = StringField('Комментарий')
  submit = SubmitField('Фильтровать')
