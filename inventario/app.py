import tkinter as tk
from tkinter import messagebox, ttk
from producto import Producto
from categoria import Categoria
from proveedor import Proveedor
from bodega import Bodega

# Definición de la clase principal App
class App:
    def __init__(self, root):
        # Constructor de la clase App
        self.root = root
        self.root.title("Gestor de Inventarios")

        # Inicializar listas
        self.productos = []
        self.categorias = []
        self.proveedores = []
        self.bodegas = []

        # Crear interfaz gráfica
        self.crear_interfaz()

    def crear_interfaz(self):
        # Crear un Notebook para pestañas
        notebook = ttk.Notebook(self.root)
        notebook.pack(padx=10, pady=10)

        # Pestaña de Productos
        frame_productos = ttk.Frame(notebook)
        notebook.add(frame_productos, text="Productos")
        self.crear_pestana_productos(frame_productos)

        # Pestaña de Categorías
        frame_categorias = ttk.Frame(notebook)
        notebook.add(frame_categorias, text="Categorías")
        self.crear_pestana_categorias(frame_categorias)

        # Pestaña de Proveedores
        frame_proveedores = ttk.Frame(notebook)
        notebook.add(frame_proveedores, text="Proveedores")
        self.crear_pestana_proveedores(frame_proveedores)

        # Pestaña de Bodegas
        frame_bodegas = ttk.Frame(notebook)
        notebook.add(frame_bodegas, text="Bodegas")
        self.crear_pestana_bodegas(frame_bodegas)

    def crear_pestana_productos(self, frame):
        # Etiqueta y campo de entrada para el nombre del producto
        tk.Label(frame, text="Nombre del Producto:").grid(row=0, column=0, sticky=tk.W)
        self.nombre_producto = tk.Entry(frame)
        self.nombre_producto.grid(row=0, column=1, sticky=tk.W)

        # Etiqueta y campo de entrada para la descripción del producto
        tk.Label(frame, text="Descripción del Producto:").grid(row=1, column=0, sticky=tk.W)
        self.descripcion_producto = tk.Entry(frame)
        self.descripcion_producto.grid(row=1, column=1, sticky=tk.W)

        # Etiqueta y campo de entrada para el precio del producto
        tk.Label(frame, text="Precio del Producto:").grid(row=2, column=0, sticky=tk.W)
        self.precio_producto = tk.Entry(frame)
        self.precio_producto.grid(row=2, column=1, sticky=tk.W)

        # Etiqueta y campo de entrada para el stock del producto
        tk.Label(frame, text="Stock del Producto:").grid(row=3, column=0, sticky=tk.W)
        self.stock_producto = tk.Entry(frame)
        self.stock_producto.grid(row=3, column=1, sticky=tk.W)

        # Etiqueta y campo de entrada para la categoría del producto
        tk.Label(frame, text="Categoría del Producto:").grid(row=4, column=0, sticky=tk.W)
        self.categoria_producto = tk.Entry(frame)
        self.categoria_producto.grid(row=4, column=1, sticky=tk.W)

        # Botón para agregar producto
        tk.Button(frame, text="Agregar Producto", command=self.agregar_producto).grid(row=5, columnspan=2, pady=5)

        # Treeview para mostrar productos
        columns = ("Nombre", "Descripción", "Precio", "Stock", "Categoría")
        self.tree_productos = ttk.Treeview(frame, columns=columns, show='headings')
        for col in columns:
            self.tree_productos.heading(col, text=col)
        self.tree_productos.grid(row=6, columnspan=2, pady=10)

    def agregar_producto(self):
        # Método para agregar un producto a la lista de productos
        nombre = self.nombre_producto.get()
        descripcion = self.descripcion_producto.get()
        precio = self.precio_producto.get()
        stock = self.stock_producto.get()
        categoria = self.categoria_producto.get()
        if nombre and descripcion and precio and stock and categoria:
            # Crear un nuevo producto con los datos ingresados
            nuevo_producto = Producto(nombre, descripcion, float(precio), int(stock), categoria)
            # Agregar el producto a la lista de productos
            self.productos.append(nuevo_producto)
            # Mostrar el producto en la interfaz gráfica
            self.tree_productos.insert('', 'end', values=(nombre, descripcion, precio, stock, categoria))
        else:
            # Mostrar una advertencia si algún campo está vacío
            messagebox.showwarning("Advertencia", "Todos los campos son obligatorios")

    def crear_pestana_categorias(self, frame):
        # Etiqueta y campo de entrada para el nombre de la categoría
        tk.Label(frame, text="Nombre de la Categoría:").grid(row=0, column=0, sticky=tk.W)
        self.nombre_categoria = tk.Entry(frame)
        self.nombre_categoria.grid(row=0, column=1, sticky=tk.W)

        # Etiqueta y campo de entrada para la descripción de la categoría
        tk.Label(frame, text="Descripción de la Categoría:").grid(row=1, column=0, sticky=tk.W)
        self.descripcion_categoria = tk.Entry(frame)
        self.descripcion_categoria.grid(row=1, column=1, sticky=tk.W)

        # Botón para agregar categoría
        tk.Button(frame, text="Agregar Categoría", command=self.agregar_categoria).grid(row=2, columnspan=2, pady=5)

        # Treeview para mostrar categorías
        columns = ("Nombre", "Descripción", "Productos")
        self.tree_categorias = ttk.Treeview(frame, columns=columns, show='headings')
        for col in columns:
            self.tree_categorias.heading(col, text=col)
        self.tree_categorias.grid(row=3, columnspan=2, pady=10)

    def agregar_categoria(self):
        # Método para agregar una categoría a la lista de categorías
        nombre = self.nombre_categoria.get()
        descripcion = self.descripcion_categoria.get()
        if nombre and descripcion:
            # Crear una nueva categoría con los datos ingresados
            nueva_categoria = Categoria(nombre, descripcion)
            # Agregar la categoría a la lista de categorías
            self.categorias.append(nueva_categoria)
            # Mostrar la categoría en la interfaz gráfica
            self.tree_categorias.insert('', 'end', values=(nombre, descripcion, ""))
        else:
            # Mostrar una advertencia si algún campo está vacío
            messagebox.showwarning("Advertencia", "Todos los campos son obligatorios")

    def crear_pestana_proveedores(self, frame):
        # Etiqueta y campo de entrada para el nombre del proveedor
        tk.Label(frame, text="Nombre del Proveedor:").grid(row=0, column=0, sticky=tk.W)
        self.nombre_proveedor = tk.Entry(frame)
        self.nombre_proveedor.grid(row=0, column=1, sticky=tk.W)

        # Etiqueta y campo de entrada para la dirección del proveedor
        tk.Label(frame, text="Dirección del Proveedor:").grid(row=1, column=0, sticky=tk.W)
        self.direccion_proveedor = tk.Entry(frame)
        self.direccion_proveedor.grid(row=1, column=1, sticky=tk.W)

        # Etiqueta y campo de entrada para el teléfono del proveedor
        tk.Label(frame, text="Teléfono del Proveedor:").grid(row=2, column=0, sticky=tk.W)
        self.telefono_proveedor = tk.Entry(frame)
        self.telefono_proveedor.grid(row=2, column=1, sticky=tk.W)

        # Botón para agregar proveedor
        tk.Button(frame, text="Agregar Proveedor", command=self.agregar_proveedor).grid(row=3, columnspan=2, pady=5)

        # Treeview para mostrar proveedores
        columns = ("Nombre", "Dirección", "Teléfono", "Productos")
        self.tree_proveedores = ttk.Treeview(frame, columns=columns, show='headings')
        for col in columns:
            self.tree_proveedores.heading(col, text=col)
        self.tree_proveedores.grid(row=4, columnspan=2, pady=10)

    def agregar_proveedor(self):
        # Método para agregar un proveedor a la lista de proveedores
        nombre = self.nombre_proveedor.get()
        direccion = self.direccion_proveedor.get()
        telefono = self.telefono_proveedor.get()
        if nombre and direccion and telefono:
            # Crear un nuevo proveedor con los datos ingresados
            nuevo_proveedor = Proveedor(nombre, direccion, telefono)
            # Agregar el proveedor a la lista de proveedores
            self.proveedores.append(nuevo_proveedor)
            # Mostrar el proveedor en la interfaz gráfica
            self.tree_proveedores.insert('', 'end', values=(nombre, direccion, telefono, ""))
        else:
            # Mostrar una advertencia si algún campo está vacío
            messagebox.showwarning("Advertencia", "Todos los campos son obligatorios")

    def crear_pestana_bodegas(self, frame):
        # Etiqueta y campo de entrada para el nombre de la bodega
        tk.Label(frame, text="Nombre de la Bodega:").grid(row=0, column=0, sticky=tk.W)
        self.nombre_bodega = tk.Entry(frame)
        self.nombre_bodega.grid(row=0, column=1, sticky=tk.W)

        # Etiqueta y campo de entrada para la ubicación de la bodega
        tk.Label(frame, text="Ubicación de la Bodega:").grid(row=1, column=0, sticky=tk.W)
        self.ubicacion_bodega = tk.Entry(frame)
        self.ubicacion_bodega.grid(row=1, column=1, sticky=tk.W)

        # Etiqueta y campo de entrada para la capacidad máxima de la bodega
        tk.Label(frame, text="Capacidad Máxima de la Bodega:").grid(row=2, column=0, sticky=tk.W)
        self.capacidad_maxima_bodega = tk.Entry(frame)
        self.capacidad_maxima_bodega.grid(row=2, column=1, sticky=tk.W)

        # Botón para agregar bodega
        tk.Button(frame, text="Agregar Bodega", command=self.agregar_bodega).grid(row=3, columnspan=2, pady=5)

        # Treeview para mostrar bodegas
        columns = ("Nombre", "Ubicación", "Capacidad Máxima", "Productos")
        self.tree_bodegas = ttk.Treeview(frame, columns=columns, show='headings')
        for col in columns:
            self.tree_bodegas.heading(col, text=col)
        self.tree_bodegas.grid(row=4, columnspan=2, pady=10)

    def agregar_bodega(self):
        # Método para agregar una bodega a la lista de bodegas
        nombre = self.nombre_bodega.get()
        ubicacion = self.ubicacion_bodega.get()
        capacidad_maxima = self.capacidad_maxima_bodega.get()
        if nombre and ubicacion and capacidad_maxima:
            # Crear una nueva bodega con los datos ingresados
            nueva_bodega = Bodega(nombre, ubicacion, int(capacidad_maxima))
            # Agregar la bodega a la lista de bodegas
            self.bodegas.append(nueva_bodega)
            # Mostrar la bodega en la interfaz gráfica
            self.tree_bodegas.insert('', 'end', values=(nombre, ubicacion, capacidad_maxima, ""))
        else:
            # Mostrar una advertencia si algún campo está vacío
            messagebox.showwarning("Advertencia", "Todos los campos son obligatorios")

if __name__ == "__main__":
    root = tk.Tk()
    app = App(root)
    root.mainloop()
