from datetime import datetime, timezone
from typing import Optional
from werkzeug.security import check_password_hash
import sqlalchemy as sa
import sqlalchemy.orm as so
from app import db

class Methodology(db.Model):
  id: so.Mapped[int] = so.mapped_column(primary_key=True)

class Conditions(db.Model):
  id: so.Mapped[int] = so.mapped_column(primary_key=True)
  date: so.Mapped[datetime] = so.mapped_column(default=lambda: datetime.now(timezone.utc))
  temperature: so.Mapped[float] = so.mapped_column(sa.Float())
  humidity: so.Mapped[float] = so.mapped_column(sa.Float())
  pressure: so.Mapped[float] = so.mapped_column(sa.Float())
  voltage: so.Mapped[Optional[float]] = so.mapped_column(sa.Float())
  frequency: so.Mapped[Optional[float]] = so.mapped_column(sa.Float())
  other: so.Mapped[Optional[str]] = so.mapped_column(sa.Text())
  location: so.Mapped[Optional[str]] = so.mapped_column(sa.String(), default='ОЦСМ')
  comment: so.Mapped[Optional[str]] = so.mapped_column(sa.String())

  def __repr__(self):
    return f'<Conditions_{self.id} date: {self.date}>'

class Engineers(db.Model):
  id: so.Mapped[int] = so.mapped_column(primary_key=True)
  number: so.Mapped[int] = so.mapped_column(sa.Integer())
  first_name: so.Mapped[str] = so.mapped_column(sa.String())
  second_name: so.Mapped[str] = so.mapped_column(sa.String())
  last_name: so.Mapped[str] = so.mapped_column(sa.String())
  birthday: so.Mapped[datetime] = so.mapped_column(sa.Date())
  department: so.Mapped[int] = so.mapped_column(sa.Integer())
  username: so.Mapped[str] = so.mapped_column(sa.String())
  password_hash: so.Mapped[str] = so.mapped_column(sa.String())

  def check_password(self, password):
    return check_password_hash(self.password_hash, password)

  def get_by_name(self, name):
    return self.query.filter_by(username=name).first()

  def __repr__(self):
    return f'<Engineer_{self.username} {self.number}>'

class Channels(db.Model):
  id: so.Mapped[int] = so.mapped_column(primary_key=True)
  methodology_id: so.Mapped[int] = so.mapped_column(sa.Integer())
  channel: so.Mapped[Optional[str]] = so.mapped_column(sa.String())
  component: so.Mapped[Optional[str]] = so.mapped_column(sa.String())


