from callmaster.app.models.data_models.client import ClientModel
from callmaster.app.models.data_models.specialist import SpecialistModel
from callmaster.app.models.database.main import AsyncSessionLocal
from callmaster.app.models.service.client import ClientService
from callmaster.app.models.service.specialist import SpecialistService

client_service = ClientService(ClientModel, AsyncSessionLocal)
specialist_service = SpecialistService(SpecialistModel, AsyncSessionLocal)
