class Proveedor:
    def __init__(self, nombre, direccion, telefono):
        # Constructor de la clase Proveedor
        self.nombre = nombre
        self.direccion = direccion
        self.telefono = telefono
        self.productos = []

    def agregar_producto(self, producto):
        # Método para agregar un producto a la lista de productos del proveedor
        self.productos.append(producto)

    def __str__(self):
        # Método para representar el objeto Proveedor como una cadena
        return f"Proveedor: {self.nombre}, Dirección: {self.direccion}, Teléfono: {self.telefono}, Productos: {[producto.nombre for producto in self.productos]}"
