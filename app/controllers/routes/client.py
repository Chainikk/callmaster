from typing import Annotated

from fastapi import APIRouter, Depends

from callmaster.app.controllers.actions.client import create_client, get_client_by_id, update_client_email, \
    update_client_phone, update_client_password
from callmaster.app.controllers.schema import UpdateEmailRequest, UpdatePhoneRequest
from callmaster.app.views.client import NewClient, ViewClient
from callmaster.app.controllers.schema import UpdatePasswordRequest

router = APIRouter(prefix='/client', tags=['client'])


@router.post("", response_model=ViewClient)
async def register_client(
        new_client: Annotated[NewClient, Depends()]
):
    return await create_client(new_client)


@router.get("/{client_id}", response_model=ViewClient)
async def get_client(
        client_id: int
):
    return await get_client_by_id(client_id)


@router.patch("/{client_id}/email")
async def update_email(client_id: int, update_request: Annotated[UpdateEmailRequest, Depends()]):
    return await update_client_email(client_id, update_request.email)


@router.patch("/{client_id}/phone")
async def update_phone(client_id: int, update_request: Annotated[UpdatePhoneRequest, Depends()]):
    return await update_client_phone(client_id, update_request.phone)


@router.patch("/{client_id}/password")
async def update_password(client_id: int, update_request: Annotated[UpdatePasswordRequest, Depends()]):
    return await update_client_password(client_id, update_request.old_password, update_request.new_password)
