from flask import Flask, render_template, request, redirect, url_for
from entidades.producto import GestionTienda, ItemCarrito
from entidades.excepciones import CantidadInvalidaError

app = Flask(__name__)
tienda = GestionTienda()
carrito_global = []

@app.route('/')
def index():
    # Muestra la página de ventas (basada en tu imagen)
    return render_template('index.html', productos=tienda.inventario)

@app.route('/agregar', methods=['POST'])
def agregar():
    try:
        prod_id = int(request.form.get('id'))
        cantidad = int(request.form.get('cantidad'))
        
        if cantidad <= 0:
            raise CantidadInvalidaError("La cantidad debe ser mayor a cero")
            
        producto = tienda.buscar_por_id(prod_id)
        if producto:
            carrito_global.append(ItemCarrito(producto, cantidad))
            
        return redirect(url_for('comprar'))
    except CantidadInvalidaError:
        return "Error: Cantidad no válida", 400

@app.route('/comprar')
def comprar():
    # Basado en tu imagen "tienda concepto 2"
    subtotal, iva, total = tienda.calcular_totales(carrito_global)
    return render_template('comprar.html', 
                           items=carrito_global, 
                           subtotal=subtotal, 
                           iva=iva, 
                           total=total)

if __name__ == '__main__':
    app.run(debug=True)