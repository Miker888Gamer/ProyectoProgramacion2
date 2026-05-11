from entidades.producto import Producto, Categoria
from entidades.excepciones import ProductoNoEncontradoError, CarritoVacioError

class Inventario:
    def __init__(self):
        
        self.productos_disponibles = [
            Producto("Bolillo de Minecraft", 15.50, Categoria.GAMER),
            Producto("Una Banana", 5.00, Categoria.COMIDA),
            Producto("Leshe Shabo", 22.00, Categoria.BEBIDA)
        ]

    def obtener_todo(self):
        return self.productos_disponibles

    def buscar(self, nombre):
        for p in self.productos_disponibles:
            if p.nombre == nombre:
                return p
        raise ProductoNoEncontradoError(f"No tenemos {nombre} en stock.")

class Carrito:
    def __init__(self):
        self.items = []

    def agregar(self, producto):
        self.items.append(producto)

    def calcular_totales(self):
        """Lógica de negocio: Calcula subtotal, IVA y total."""
        if not self.items:
            raise CarritoVacioError("El carrito está vacío.")
            
        subtotal = sum(p.precio for p in self.items)
        iva = subtotal * 0.16
        return {
            "subtotal": round(subtotal, 2),
            "iva": round(iva, 2),
            "total": round(subtotal + iva, 2)
        }