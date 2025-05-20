from app import app, db
from app.models import Conditions, Engineers
import sqlalchemy as sa
from werkzeug.security import generate_password_hash, check_password_hash
from importlib import import_module, reload
import sys

models = import_module('app.models')

reload(models)

print(sys.modules)

app.app_context().push()

c = Conditions(temperature=20.4, humidity=49.2, pressure=101.3)
c

query = sa.select(Engineers)
eng = db.session.scalars(query).all()

eng[0].password_hash = generate_password_hash(f'{eng[0].number:02}56')

for e in eng:
  e.password_hash = generate_password_hash(f'{e.number:02}56')
  #check_password_hash(e.password_hash, f'{e.number:02}56')

for i in [0, 1, 2]:
  print(i ** 2)

generate_password_hash(f'{eng[0].number:02}56')



db.session.rollback()

db.session.commit()

print(f'{eng[0].number:02}')

query = sa.select(Conditions).where(Conditions.date > '2024-07-15')
query = query.where(Conditions.id > 1264)
cs = db.session.scalars(query).all()
cs
