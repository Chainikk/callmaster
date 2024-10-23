from callmaster.app.views.specialist import NewSpecialist, ViewSpecialist
from callmaster.app.models.service import specialist_service


async def create_specialist(new_specialist: NewSpecialist) -> ViewSpecialist:
    created_specialist = await specialist_service.register(new_specialist.model_dump())
    return ViewSpecialist.model_validate(created_specialist)


async def get_specialist_by_id(specialist_id: int):
    specialist = await specialist_service.get_specialist(specialist_id)
    return specialist


async def update_specialist_email(specialist_id: int, email: str):
    await specialist_service.update_email(specialist_id, email)