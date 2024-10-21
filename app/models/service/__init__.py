from models.data_models.client import ClientModel
from models.database.main import AsyncSessionLocal
from models.service.client import ClientService

client_service = ClientService(ClientModel, AsyncSessionLocal)
