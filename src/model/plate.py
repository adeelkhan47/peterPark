from sqlalchemy.sql.schema import Column
from sqlalchemy.sql.sqltypes import String, DateTime

from model.base import Base, db


class Plate(Base, db.Model):
    __tablename__ = "plate"
    plate = Column(String, nullable=False)
    start_date = Column(DateTime, nullable=True, default=None)
    end_date = Column(DateTime, nullable=True, default=None)
    owner_name = Column(String, nullable=True, default=None)

    # def __init__(self, plate, start_date, end_date, owner_name):
    #     self.plate = plate
    #     self.start_date = start_date
    #     self.end_date = end_date
    #     self.owner_name = owner_name

    def __repr__(self):
        return '<id {}>'.format(self.id)
