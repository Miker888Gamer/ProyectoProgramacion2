from entidades.producto import Producto, TipoProducto

class GestorCobro:
    """Clase para manejar los cálculos de la compra."""

    def __init__(self):
        # Usamos una lista como colección (Requisito 4)
        self.carrito: list[Producto] = []

    def agregar_producto(self, producto: Producto) -> None:
        self.carrito.append(producto)

    def calcular_descuento(self, producto: Producto) -> float:
        """Aplica 10% de descuento si es lácteo."""
        if producto.tipo == TipoProducto.LACTEO:
            return producto.precio * 0.10
        return 0.0

    def obtener_totales(self) -> dict:
        subtotal = 0.0
        total_descuento = 0.0
        
        for p in self.carrito:
            subtotal += p.precio
            total_descuento += self.calcular_descuento(p)
        
        iva = (subtotal - total_descuento) * 0.16
        total = (subtotal - total_descuento) + iva
        
        return {
            "subtotal": round(subtotal, 2),
            "descuento": round(total_descuento, 2),
            "iva": round(iva, 2),
            "total": round(total, 2)
        }