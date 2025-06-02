from flask import flash, session, render_template, redirect, url_for, request
from app.auth import bp
from app.auth.forms import LoginForm
import app.models as m

@bp.route('/login', methods=['GET', 'POST'])
def login():
  form = LoginForm()

  if form.validate_on_submit():
    #user = m.Engineers.query.filter_by(username=form.username.data).first()
    user = m.Engineers().get_by_name(form.username.data)
    
    if user is None or not user.check_password(form.password.data):
      flash('Invalid username or password')
      return redirect(url_for('auth.login'))

    flash(f'Login requested for user={form.username.data}')
    session['logged_in'] = True
    session['username'] = user.username
    session['user_id'] = user.id
    session['current_page'] = "verifications"
    return redirect(url_for('index'))
  return render_template('auth/login.html', title='Войти', form=form)

@bp.route('/logout')
def logout():
  session.pop('logged_in', None)
  session.pop('username', None)
  session.pop('user_id', None)
  session.pop('current_page', None)
  flash('Войдите в систему под своей учетной записью.')
  return redirect(url_for('auth.login'))
