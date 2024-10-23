from sqlalchemy import select, update
from sqlalchemy.ext.asyncio import AsyncEngine

from callmaster.app.models.data_models.specialist import SpecialistModel


class SpecialistService:
    def __init__(self, specialist_model: SpecialistModel, database_engine: AsyncEngine):
        self._specialist_model = specialist_model
        self._database_engine = database_engine

    async def register(self, new_specialist: dict) -> SpecialistModel:

        async with self._database_engine() as session:
            try:
                specialist_model = self._specialist_model(**new_specialist)
                session.add(specialist_model)
                await session.commit()
                await session.refresh(specialist_model)
                return specialist_model
            except Exception as e:
                await session.rollback()
                raise

    async def get_specialist(self, specialist_id: int) -> SpecialistModel:
        async with self._database_engine() as session:
            try:
                query = select(self._specialist_model).where(
                    self._specialist_model.id == specialist_id
                )
                result = await session.execute(query)
                specialist = result.scalars().first()
                return specialist
            except Exception as e:
                raise e

    async def update_email(self, specialist_id: int, new_email: str) -> None:
        async with self._database_engine() as session:
            try:
                # осущетсвить првоерку формата почты перед сменой
                stmt = (
                    update(self._specialist_model)
                    .where(self._specialist_model.id == specialist_id)
                    .values(email=new_email)
                )
                await session.execute(stmt)
                await session.commit()
            except Exception as e:
                await session.rollback()
                raise e
