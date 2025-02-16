# session.py
from cassandraConeccion import AstraDBConnection
from datetime import datetime

class Session:
    def __init__(self):
        self.astra_db = AstraDBConnection()
        self.collection_name = "Session"

    def create_collection(self):
        if self.collection_name not in self.astra_db.db.list_collection_names():
            self.astra_db.create_collection(self.collection_name)
            print(f"Colección '{self.collection_name}' creada.")

    def insert_initial_data(self):
        if self.collection_name not in self.astra_db.db.list_collection_names():
            session_data = [
                {"id_sesion": 1, "id_cliente": 1, "inicio": "2025-01-01T00:00:00", "fin": "2025-01-02T00:00:00", "id_solicitud": 1},
                {"id_sesion": 2, "id_cliente": 2, "inicio": "2025-01-03T00:00:00", "fin": "2025-01-04T00:00:00", "id_solicitud": 2},
                {"id_sesion": 3, "id_cliente": 3, "inicio": "2025-01-05T00:00:00", "fin": "2025-01-06T00:00:00", "id_solicitud": 3},
                {"id_sesion": 4, "id_cliente": 4, "inicio": "2025-01-07T00:00:00", "fin": "2025-01-08T00:00:00", "id_solicitud": 4},
                {"id_sesion": 5, "id_cliente": 5, "inicio": "2025-01-09T00:00:00", "fin": "2025-01-10T00:00:00", "id_solicitud": 5},
            ]
            self.astra_db.insert_many(self.collection_name, session_data)
            print(f"Datos insertados en '{self.collection_name}'.")
    
    def iniciar_session(self,id_cliente):
        try:
            inicio= datetime.now()
            session=[{"id_cliente":id_cliente,"inicio":inicio}]
            self.astra_db.insert_many(self.collection_name,session)
            return True
        except Exception as e:
            print("no pudo registrarse la session "+e)

            return False
    def cerrar_session(self,id_cliente):
        try:
            fin=datetime.now()
            session=[{"id_cliente":id_cliente,"fin":fin}]
            self.astra_db.insert_many(self.collection_name,session)
            return True        
        except Exception as e:
            print("no se pudo definir el cierre de sesión "+e)

    def nueva_solicitud(self,id_cliente,id_solicitud):
        filtro={"id_cliente":id_cliente}
        #agregar el filtro de buscar la última solicitud
        try:
            sesion_existente=self.astra_db.find(self.collection_name,filtro)
            ultima=sesion_existente[-1]
            filtroUltima={"id_sesion":ultima.get("id_sesion")}

            insertar={"$set":{"id_solicitud":id_solicitud}}
            try:
                self.astra_db[self.collection_name].update_one(filtroUltima,insertar)
            except Exception as i:
                print("no se pudo asignar la solicitud a la session "+ i)
            return False
        
        except Exception as e:
            print("no se pudo asignar la solicitud a la session "+e)
            return False
    
    def ultima_solicitud(self,id_cliente):
        filtro={"id_cliente":id_cliente}
        try:
            sesiones_existentes=self.astra_db.find(self.collection_name,filtro)
            ultima=sesiones_existentes[-1].get("id_sesion")
            print("última session del usuario: "+ultima)
            return ultima
        
        except Exception as e:
            print("no se encontró sesión "+e )
            return False
    
    def todas_sesiones(self,id_cliente):
        filtro={"id_cliente":id_cliente}
        try:
            sesiones_existentes=self.astra_db.find(self.collection_name,filtro)
            return list(sesiones_existentes)
        except Exception as e:
            print("no se encontraron sesiones "+e)
    
    def find_all(self):
        documents = self.astra_db.find(self.collection_name)
        for doc in documents:
            print(doc)