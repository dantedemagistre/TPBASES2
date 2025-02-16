# main.py
from catalogo import Catalogo

catalogo=Catalogo()


#print("Datos en 'Catalogo':")
#for doc in catalogo.find_all():    print(doc)

#el precio del producto con id 2
#print(catalogo.conocerPrecio(2))
"""
print("precio iniciar")
print(catalogo.conocerPrecio(2) )
print("modificacion:")
print(catalogo.cambiarPrecio(2,123456) )
"""
"""
print("stock inicial:")
print(catalogo.conocerStock(2))
print("modifiación stock")
print(catalogo.cambiarStock(2,0))
"""
print(catalogo.restarAlStockActual(2,6060606060))
#conocer el stock del producto co id 3
#print(catalogo.conocerStock(100))