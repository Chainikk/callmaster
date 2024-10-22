from datetime import datetime
from enum import Enum
from typing import List

from pydantic import BaseModel, ConfigDict


class SpecializationEnum(str, Enum):
    electrician = 'electrician'
    plumber = 'plumber'


class NewSpecialist(BaseModel):
    last_name: str
    first_name: str
    middle_name: str
    email: str
    phone_number: str
    password: str
    specialization: SpecializationEnum


class SavedSpecialist(NewSpecialist):
    model_config = ConfigDict(
        from_attributes=True
    )

    id: int
    timestamp: datetime


class ViewSpecialist(SavedSpecialist):
    model_config = ConfigDict(
        fields=[
            {'password': {'exclude': True}}
        ]
    )
