class Categoria:
    def __init__(self, nombre, descripcion):
        # Constructor de la clase Categoría
        self.nombre = nombre
        self.descripcion = descripcion
        self.productos = []

    def agregar_producto(self, producto):
        # Método para agregar un producto a la categoría
        self.productos.append(producto)

    def __str__(self):
        # Método para representar el objeto Categoría como una cadena
        return f"Categoría: {self.nombre}, Descripción: {self.descripcion}, Productos: {[producto.nombre for producto in self.productos]}"
