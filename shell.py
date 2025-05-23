from importlib import import_module, reload
import sys
import sqlalchemy as sa
from werkzeug.security import generate_password_hash, check_password_hash

app = import_module('app')
m = import_module('app.models')

reload(app)
reload(m)

app.app_context().push()

c = m.Conditions(temperature=20.4, humidity=49.2, pressure=101.3)
c

query = sa.select(Engineers)
eng = app.db.session.scalars(query).all()

eng[0].password_hash = generate_password_hash(f'{eng[0].number:02}56')

for e in eng:
  e.password_hash = generate_password_hash(f'{e.number:02}56')
  #check_password_hash(e.password_hash, f'{e.number:02}56')

for i in [0, 1, 2]:
  print(i ** 2)

generate_password_hash(f'{eng[0].number:02}56')



app.db.session.rollback()

app.db.session.commit()

query = sa.select(m.Conditions).where(m.Conditions.date > '2024-07-15')
query = query.where(m.Conditions.id > 1264)
cs = app.db.session.scalars(query).all()
cs
