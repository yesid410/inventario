class Producto:
    def __init__(self, nombre, descripcion, precio, stock, categoria):
        # Constructor de la clase Producto
        self.nombre = nombre
        self.descripcion = descripcion
        self.precio = precio
        self.stock = stock
        self.categoria = categoria

    def __str__(self):
        # Método para representar el objeto Producto como una cadena
        return f"Producto: {self.nombre}, Descripción: {self.descripcion}, Precio: {self.precio}, Stock: {self.stock}, Categoría: {self.categoria}"
