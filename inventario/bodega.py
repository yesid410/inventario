class Bodega:
    def __init__(self, nombre, ubicacion, capacidad_maxima):
        # Constructor de la clase Bodega
        self.nombre = nombre
        self.ubicacion = ubicacion
        self.capacidad_maxima = capacidad_maxima
        self.productos = []

    def agregar_producto(self, producto, cantidad):
        # Método para agregar productos a la bodega
        if len(self.productos) + cantidad <= self.capacidad_maxima:
            self.productos.append((producto, cantidad))
        else:
            print("No hay suficiente espacio en la bodega")

    def __str__(self):
        # Método para representar el objeto Bodega como una cadena
        return f"Bodega: {self.nombre}, Ubicación: {self.ubicacion}, Capacidad Máxima: {self.capacidad_maxima}, Productos: {[producto[0].nombre for producto in self.productos]}"
