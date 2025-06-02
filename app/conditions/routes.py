from flask import render_template, flash, redirect, url_for, session, request
from app import db
from app.conditions import bp
from app.conditions.forms import ConditionsFilter
import app.models as m
from sqlalchemy import select, desc
from config import Config

@bp.route('/conditions', methods=['GET', 'POST'])
def conditions():
  form = ConditionsFilter()
  stmt = select(m.Conditions)

  if form.validate_on_submit():
    date_from = form.date_from.data
    date_to = form.date_to.data
    location = form.location.data
    comment = form.comment.data

    if date_from:
      stmt = stmt.where(m.Conditions.date > date_from)
    if date_to:
      stmt = stmt.where(m.Conditions.date < date_to)
    if location:
      stmt = stmt.where(m.Conditions.location.like(f'%{location}%'))
    if comment:
      stmt = stmt.where(m.Conditions.comment.like(f'%{comment}%'))

  if not session.get('logged_in'):
    return redirect(url_for('auth.login'))
  if request.method == 'POST':
    filters = {
      'date_from': request.form.get('date_from'),
      'date_to': request.form.get('date_to'),
      'location': request.form.get('location'),
      'comment': request.form.get('comment')
    }

  stmt = stmt.order_by(desc(m.Conditions.date))
  data = db.session.scalars(stmt.limit(Config.RECORDS_LIMIT)).all()
  return render_template('conditions/conditions.html', title="Условия поверки",
    username=session.get('username'),
    data = data, form = form)
