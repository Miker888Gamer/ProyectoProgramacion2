class ProductoNoEncontradoError(Exception):
    """Excepción cuando se busca un ID que no existe."""
    pass

class CantidadInvalidaError(Exception):
    """Excepción cuando el usuario pide 0 o menos productos."""
    pass