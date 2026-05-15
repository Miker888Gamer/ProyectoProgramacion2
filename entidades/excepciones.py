class CarritoVacioError(Exception):
    """Se lanza cuando se intenta comprar sin productos."""
    pass

class ProductoInvalidoError(Exception):
    """Se lanza si hay un error con los datos del producto."""
    pass