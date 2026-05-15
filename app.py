from flask import Flask, render_template, request, redirect, url_for
from entidades.producto import Producto, TipoProducto
from entidades.descuento import GestorCobro
from entidades.excepciones import CarritoVacioError

app = Flask(__name__)

# Base de datos simulada
catalogo = {
    "1": Producto("café", 20.0, TipoProducto.CAFE, "cafe.jpg"),
    "2": Producto("frappe", 10.0, TipoProducto.FRAPPE, "frappe.jpg"),
    "3": Producto("cafe con leche", 15.0, TipoProducto.LACTEO, "cafe_leche.jpg")
}

@app.route('/')
def index():
    return render_template('index.html', productos=catalogo)

@app.route('/comprar', methods=['POST'])
def comprar():
    gestor = GestorCobro()
    
    # Recogemos las cantidades del formulario
    try:
        hay_productos = False
        for id_prod, producto in catalogo.items():
            cantidad = int(request.form.get(f'cant_{id_prod}', 0))
            if cantidad > 0:
                hay_productos = True
                for _ in range(cantidad):
                    gestor.agregar_producto(producto)
        
        if not hay_productos:
            raise CarritoVacioError("No seleccionaste nada.")
            
        resumen = gestor.obtener_totales()
        return render_template('comprar.html', resumen=resumen, items=gestor.carrito)
    
    except CarritoVacioError:
        return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)