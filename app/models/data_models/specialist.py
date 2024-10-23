from datetime import datetime
from sqlalchemy import Column, Integer, String, DateTime, Enum

from callmaster.app.models.data_models.main import Base


class SpecialistModel(Base):
    __tablename__ = 'specialists'

    id = Column(Integer, primary_key=True, index=True)
    first_name = Column(String, nullable=False)
    last_name = Column(String, nullable=False)
    middle_name = Column(String, nullable=False)
    email = Column(String, nullable=False, unique=True)
    phone_number = Column(String, nullable=False, unique=True)
    password = Column(String, nullable=False)
    specialization = Column(String, nullable=False)
    timestamp = Column(DateTime, default=datetime.now)

    def __repr__(self):
        return (f"Client(id={self.id}, first_name={self.first_name}, last_name={self.last_name}, "
                f"middle_name={self.middle_name}, email={self.email}, phone_number={self.phone_number}, "
                f"specialization={self.specialization})")
