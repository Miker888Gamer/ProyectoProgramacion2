from enum import Enum

class TipoProducto(Enum):
    CAFE = "Café"
    LACTEO = "Lácteo"
    FRAPPE = "Frappé"

class Producto:
    """Clase que representa un producto de la cafetería."""
    
    def __init__(self, nombre: str, precio: float, tipo: TipoProducto, imagen: str):
        self.nombre: str = nombre
        self.precio: float = precio
        self.tipo: TipoProducto = tipo
        self.imagen: str = imagen

    def __str__(self) -> str:
        return f"{self.nombre} - ${self.precio}"