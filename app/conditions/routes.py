from flask import render_template, flash, redirect, url_for, session, request
from app import db
from app.conditions import bp
from app.conditions.forms import ConditionsFilter
import app.models as m
from sqlalchemy import select, desc, func, or_
from config import Config

@bp.route('/conditions', methods=['GET', 'POST'])
def conditions():
  form = ConditionsFilter()
  stmt = select(m.Conditions)
  filters = {
    'page': 1,
    'date_from': '',
    'date_to': '',
    'location': '',
    'comment': ''
  }

  if not session.get('logged_in'):
    return redirect(url_for('auth.login'))
  if request.method == 'POST':
    filters = {
      'page': request.form.get('page'),
      'date_from': request.form.get('date_from'),
      'date_to': request.form.get('date_to'),
      'location': request.form.get('location'),
      'comment': request.form.get('comment')
    }

  if filters['date_from'] != '':
    stmt = stmt.where(m.Conditions.date > filters['date_from'])
  if filters['date_to'] != '':
    stmt = stmt.where(m.Conditions.date < filters['date_to'])

  stmt = (
    stmt.where(or_(m.Conditions.location.like(f'%{filters["location"]}%'),
                  m.Conditions.location == None))
    .where(or_(m.Conditions.comment.like(f'%{filters["comment"]}%'),
              m.Conditions.comment == None))
    .order_by(desc(m.Conditions.date))
    .limit(Config.RECORDS_LIMIT)
    .offset((int(filters['page']) - 1) * Config.RECORDS_LIMIT)
  )

  data = db.session.scalars(stmt).all()

  count = (db.session.scalars(select(func.count(m.Conditions.id))).first())

  return render_template('conditions/conditions.html', title="Условия поверки",
    username=session.get('username'),
    data = data, count = count, form = form)
