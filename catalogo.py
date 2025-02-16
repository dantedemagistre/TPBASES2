# catalogo.py
from cassandraConeccion import AstraDBConnection

class Catalogo:
    def __init__(self):
        self.astra_db = AstraDBConnection()
        self.collection_name = "Catalogo"

    def create_collection(self):
        """Crea la colección 'Catalogo' si no existe."""
        if self.collection_name not in self.astra_db.db.list_collection_names():
            self.astra_db.create_collection(self.collection_name)
            print(f"Colección '{self.collection_name}' creada.")

    def insert_initial_data(self):
        """Inserta datos iniciales en la colección 'Catalogo'."""
        catalogo_data = [
            {"id_catalogo": 1, "id_producto": 1, "stock": 100, "precio": 50},
            {"id_catalogo": 2, "id_producto": 2, "stock": 150, "precio": 75},
            {"id_catalogo": 3, "id_producto": 3, "stock": 200, "precio": 100},
            {"id_catalogo": 4, "id_producto": 4, "stock": 250, "precio": 125},
            {"id_catalogo": 5, "id_producto": 5, "stock": 300, "precio": 150},
        ]
        self.astra_db.insert_many(self.collection_name, catalogo_data)
        print(f"Datos insertados en '{self.collection_name}'.")

    def conocerPrecio(self, id_producto):
        query = {"id_producto": id_producto}
        documents = self.astra_db.find(self.collection_name, query)
        for doc in documents:
            return doc.get('precio')
        return None  # Si no se encuentra el producto

    def cambiarPrecio(self, id_producto, precioNuevo):
        query = {"id_producto": id_producto}
        if precioNuevo>=1:
            update = {"$set": {"precio": precioNuevo}}  # Operación de actualización
            try:
                resultado = self.astra_db.db[self.collection_name].update_one(query, update)
                if resultado:
                    print(f"Precio del producto {id_producto} actualizado a {precioNuevo}.")
                    return True
                else:
                    print(f"No se encontró ningún producto con id {id_producto}.")
                    return False
            except Exception as e:
                print(f"Error al actualizar el precio: {e}")
                return False
        else: 
            print("no se pueden definir precios negativos ni cero")
            return False

    def conocerStock(self, id_producto):
        query = {"id_producto": id_producto}
        documents = self.astra_db.find(self.collection_name, query)
        for doc in documents:
            return doc.get('stock')
        return None  # Si no se encuentra el producto
    
    def cambiarStock(self, id_producto, stockNuevo):
#           verificar que el stock a definir sea válido
        if stockNuevo >=0:
        
            query={"id_producto":id_producto}
            update={"$set":{"stock":stockNuevo}}
            try:
                resultado = self.astra_db.db[self.collection_name].update_one(query, update)
                if resultado:
                    print(f"stock del producto {id_producto} actualizado a {stockNuevo}.")
                    return True
                else:
                    print(f"No se encontró ningún producto con id {id_producto}.")
                    return False
            except Exception as e:
                print(f"Error al actualizar el stock: {e}")
                return False
        else:
            print(" no se pueden definir stock menores que  cero")
            return False    

    def restarAlStockActual(self,id_producto,cantidad_a_restar):
        query={"id_producto":id_producto}
        producto = self.astra_db.find(self.collection_name, query)
        cantidad_actual=0

        for p in producto:
            cantidad_actual=p.get("stock")

        resultado=cantidad_actual - cantidad_a_restar
        if resultado >=0:
            update={"$set":{"stock":resultado}}
            try:
                self.astra_db.db[self.collection_name].update_one(query, update)
                print(f'se actualizó el stock del producto a {resultado}')
                return True
            
            except Exception as e:

                print(f"No se encontró ningún producto con id {id_producto},{e}.")
                return False
        else:
            print(" no se pueden definir stock menores que  cero")
            return False    

    def  sumarAlStockActual(self,id_producto,cantidad_a_sumar):
        if cantidad_a_sumar>0:
            query={"id_producto":id_producto}
            producto = self.astra_db.find_one(self.collection_name, query)
            cantidad_actual=0
            for p in producto:
                cantidad_actual=p.get("stock")
            resultado=cantidad_actual + cantidad_a_sumar
            update={"$set":{"stock":resultado}}
            try:
                self.astra_db.db[self.collection_name].update_one(query, update)
                print(f'se actualizó el stock del producto a {resultado}')
                return True
            
            except Exception as e:

                print(f"No se encontró ningún producto con id {id_producto},{e}.")
                return False
        else:
            print("no se pueden sumar negativos")
            return False
    def find_all(self):
        documents = self.astra_db.find(self.collection_name)
        return list(documents)  # Convertir el cursor a una lista