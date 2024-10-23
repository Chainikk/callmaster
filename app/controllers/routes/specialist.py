from typing import Annotated

from fastapi import APIRouter, Depends

from callmaster.app.controllers.actions.specialist import create_specialist, get_specialist_by_id, \
    update_specialist_email, update_specialist_phone, update_specialist_password
from callmaster.app.controllers.schema import UpdateEmailRequest, UpdatePhoneRequest
from callmaster.app.views.specialist import NewSpecialist, ViewSpecialist
from callmaster.app.controllers.schema import UpdatePasswordRequest

router = APIRouter(prefix='/specialist', tags=['specialist'])


@router.post("", response_model=ViewSpecialist)
async def register_specialist(
        new_specialist: Annotated[NewSpecialist, Depends()]
):
    return await create_specialist(new_specialist)


@router.get("/{specialist_id}", response_model=ViewSpecialist)
async def get_specialist(
        specialist_id: int
):
    return await get_specialist_by_id(specialist_id)


@router.patch("/{specialist_id}/email")
async def update_email(specialist_id: int, update_request: Annotated[UpdateEmailRequest, Depends()]):
    return await update_specialist_email(specialist_id, update_request.email)


@router.patch("/{specialist_id}/phone")
async def update_phone(specialist_id: int, update_request: Annotated[UpdatePhoneRequest, Depends()]):
    return await update_specialist_phone(specialist_id, update_request.phone)


@router.patch("/{specialist_id}/password")
async def update_password(specialist_id: int, update_request: Annotated[UpdatePasswordRequest, Depends()]):
    return await update_specialist_password(specialist_id, update_request.old_password, update_request.new_password)
