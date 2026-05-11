from enum import Enum

# 1. Enumerador para categorías
class Categoria(Enum):
    ABARROTES = "Abarrotes"
    PANADERIA = "Panadería"
    FRUTA = "Fruta"

# 2. Clase de Entidad
class Producto:
    """Clase que representa un producto de la tienda."""
    def __init__(self, id, nombre, precio, categoria, imagen):
        self.id = id
        self.nombre = nombre
        self.precio = precio
        self.categoria = categoria
        self.imagen = imagen

# 3. Clase de Entidad: Carrito
class ItemCarrito:
    """Representa un producto seleccionado y su cantidad."""
    def __init__(self, producto, cantidad):
        self.producto = producto
        self.cantidad = cantidad

# 4. Clase de Entidad: Tienda
class GestionTienda:
    """Clase para separar la lógica de negocio (Requisito: separar lógica)"""
    def __init__(self):
       
        self.inventario = [
            Producto(1, "leche", 20.00, Categoria.ABARROTES, "leche_shabo.jpg"),
            Producto(2, "pan", 10.00, Categoria.PANADERIA, "bolillo_minecraft.jpg"),
            Producto(3, "banana", 15.00, Categoria.FRUTA, "banana.jpg")
        ]
    
    def buscar_por_id(self, id):
        return next((p for p in self.inventario if p.id == id), None)

    def calcular_totales(self, carrito_items):
        subtotal = sum(item.producto.precio * item.cantidad for item in carrito_items)
        iva = subtotal * 0.16
        total = subtotal + iva
        return round(subtotal, 2), round(iva, 2), round(total, 2)