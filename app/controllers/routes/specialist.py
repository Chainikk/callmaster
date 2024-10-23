from typing import Annotated

from fastapi import APIRouter, Depends

from callmaster.app.controllers.actions.specialist import create_specialist, get_specialist_by_id, \
    update_specialist_email
from callmaster.app.controllers.schema import UpdateEmailRequest, UpdatePhoneRequest
from callmaster.app.views.specialist import NewSpecialist, ViewSpecialist
from callmaster.app.controllers.schema import UpdatePasswordRequest

router = APIRouter(prefix='/specialist', tags=['specialist'])


@router.post("", response_model=ViewSpecialist)
async def register_specialist(
        new_specialist: Annotated[NewSpecialist, Depends()]
):
    return await create_specialist(new_specialist)


@router.get("/{client_id}", response_model=ViewSpecialist)
async def get_specialist(
        specialist_id: int
):
    return await get_specialist_by_id(specialist_id)


@router.patch("/{client_id}/email")
async def update_email(specialist_id: int, update_request: Annotated[UpdateEmailRequest, Depends()]):
    return await update_specialist_email(specialist_id, update_request.email)
