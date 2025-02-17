# database.py
from astrapy import DataAPIClient ,constants

class AstraDBConnection:
    # Configuración de conexión con AstraDB
    ASTRA_DB_APPLICATION_TOKEN = "AstraCS:xuFEToNROlsnudqMjqjbZPXc:0db55e893cccea5607ebd6b0a2ba3e704e2d8ecf30019a792c46c6b05de1b9be"
    ASTRA_DB_API_ENDPOINT = "https://d1a4c2f5-b290-4298-bb9b-e8b2745a53a8-us-east-2.apps.astra.datastax.com"

    def __init__(self):
        # Inicializar el cliente con la configuración definida
        self.client = DataAPIClient(self.ASTRA_DB_APPLICATION_TOKEN)
        self.db = self.client.get_database_by_api_endpoint(self.ASTRA_DB_API_ENDPOINT)

    def get_collection(self, collection_name):
        return self.db.get_collection(collection_name)

    def create_collection(self, collection_name):
        return self.db.create_collection(collection_name)

    def insert_many(self, collection_name, data):
        collection = self.get_collection(collection_name)
        return collection.insert_many(data)

    def find(self, collection_name, query=None):
        collection = self.get_collection(collection_name)
        return collection.find(query)
    
    