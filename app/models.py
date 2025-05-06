from datetime import datetime, timezone
from typing import Optional
import sqlalchemy as sa
import sqlalchemy.orm as so
from app import db

class Condition(db.Model):
  id: so.Mapped[int] = so.mapped_column(primary_key=True)
  date: so.Mapped[datetime] = so.mapped_column(default=lambda: datetime.now(timezone.utc))
  temperature: so.Mapped[float] = so.mapped_column(sa.Float())
  humidity: so.Mapped[float] = so.mapped_column(sa.Float())
  pressure: so.Mapped[float] = so.mapped_column(sa.Float())

  def __repr__(self):
    return f'<Condition {self.id}>'