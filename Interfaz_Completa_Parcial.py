import tkinter as tk
from tkinter import ttk
from negocio.autor_negocio import AutorNegocio
from negocio.libro_negocio import LibroNegocio
from negocio.categoria_negocio import CategoriaNegocio

#clase principal de la aplicación
class MainMenuApp:
    # Variables de clase para almacenar instancias de negocios y listas
    negocio_autor = AutorNegocio()
    negocio_libro = LibroNegocio()
    negocio_categoria = CategoriaNegocio()
    listado_autores = []
    listado_libros = []
    listado_categorias = []
    treeview = []  # Lista para almacenar un objeto Treeview
    detalle_label = []  # Lista para almacenar un objeto Label

    # Constructor de la clase
    def __init__(self, root):
        # Configuración inicial de la ventana principal
        self.root = root
        self.root.title("Interfaz con Panel de Opciones y Contenido")
        self.root.config(bg='white')
        self.root.geometry('800x650')
        self.root.rowconfigure(0, weight=1)
        self.root.columnconfigure(0, weight=1)

        # Crear el contenedor principal
        self.container = ttk.Frame(root)
        self.container.pack(fill="both", expand=True)

        # Crear el panel de opciones en el lado izquierdo
        self.options_panel = ttk.Frame(self.container, width=150)
        self.options_panel.pack(side="left", fill="y")

        # Crear el área de contenido en el lado derecho
        self.content_frame = ttk.Frame(self.container)
        self.content_frame.pack(side="right", fill="both", expand=True)

        # Crear el menú en el panel de opciones
        self.opciones_menu = tk.Menu(self.root)
        self.root.config(menu=self.opciones_menu)
        self.opciones_menu.add_command(label="Autores", command=self.mostrar_contenido_opcion_autor)
        self.opciones_menu.add_command(label="Libros", command=self.mostrar_contenido_opcion_libro)
        self.opciones_menu.add_command(label="Categorías", command=self.mostrar_contenido_opcion_categoria)

#CONTENIDO AUTOR
    def mostrar_contenido_opcion_autor(self):
        self.limpiar_contenido()         # Limpia el contenido anterior
        # Crea un objeto Treeview para mostrar datos
        self.treeview = ttk.Treeview(self.content_frame)
        self.treeview.pack(fill="both", expand=True)

        # Configuración de columnas y encabezados del Treeview
        self.treeview["columns"] = ("Código Persona", "Nombre", "Apellido Paterno", "Apellido Materno")
        self.treeview.column("#0", width=50)
        self.treeview.column("Código Persona", width=100)
        self.treeview.column("Nombre", width=200)
        self.treeview.column("Apellido Paterno", width=150)
        self.treeview.column("Apellido Materno", width=150)

        self.treeview.heading("#0", text="Índice")
        self.treeview.heading("Código Persona", text="Código Persona")
        self.treeview.heading("Nombre", text="Nombre")
        self.treeview.heading("Apellido Paterno", text="Apellido Paterno")
        self.treeview.heading("Apellido Materno", text="Apellido Materno")
        
        # Obtención de datos de autores y llenado del Treeview
        autores = self.negocio_autor.obtener_autores()

        for i, autor in enumerate(autores):
            self.treeview.insert("", "end", text=i, values=(autor.cod_persona, autor.nombre, autor.apellido_paterno, autor.apellido_materno))
        
        # Creación de botones y etiquetas
        detalle_button = ttk.Button(self.content_frame, text="Mostrar Detalle", command=self.mostrar_detalle_autor)
        detalle_button.pack(pady=10)

        nuevo_autor_button = ttk.Button(self.content_frame, text="Nuevo Registro", command=self.nuevo_autor)
        nuevo_autor_button.pack(pady=10)
        
        editar_autor_button = ttk.Button(self.content_frame, text="Editar Registro", command=self.editar_autor)
        editar_autor_button.pack(pady=10)
        
        eliminar_autor_button = ttk.Button(self.content_frame, text="Eliminar Registro", command=self.eliminar_autor)
        eliminar_autor_button.pack(pady=10)

        # Etiqueta para mostrar detalles de autor
        self.detalle_label = ttk.Label(self.content_frame, text="")
        self.detalle_label.pack(padx=20, pady=20)

    # Función para mostrar el detalle de un autor seleccionado
    def mostrar_detalle_autor(self):
        seleccionado = self.treeview.selection()
        if seleccionado:
            indice = int(self.treeview.item(seleccionado)['text'])
            autor = self.negocio_autor.obtener_autores()[indice]
            self.detalle_label.config(text=f"Código Persona: {autor.cod_persona}\nNombre: {autor.nombre}\nApellido Paterno: {autor.apellido_paterno}\nApellido Materno: {autor.apellido_materno}")
        else:
            self.detalle_label.config(text="Seleccione un autor")
    # Función para agregar un nuevo autor
    def nuevo_autor(self):
        self.limpiar_contenido()
        # Etiquetas y campos de entrada
        self.cod_persona_label = ttk.Label(self.content_frame, text="Código de Persona:")
        self.cod_persona_label.pack()
        self.cod_persona_entry = ttk.Entry(self.content_frame)
        self.cod_persona_entry.pack()

        self.nombre_label = ttk.Label(self.content_frame, text="Nombre:")
        self.nombre_label.pack()
        self.nombre_entry = ttk.Entry(self.content_frame)
        self.nombre_entry.pack()

        self.apellido_paterno_label = ttk.Label(self.content_frame, text="Apellido Paterno:")
        self.apellido_paterno_label.pack()
        self.apellido_paterno_entry = ttk.Entry(self.content_frame)
        self.apellido_paterno_entry.pack()

        self.apellido_materno_label = ttk.Label(self.content_frame, text="Apellido Materno:")
        self.apellido_materno_label.pack()
        self.apellido_materno_entry = ttk.Entry(self.content_frame)
        self.apellido_materno_entry.pack()

        self.fecha_nacimiento_label = ttk.Label(self.content_frame, text="Fecha de Nacimiento:")
        self.fecha_nacimiento_label.pack()
        self.fecha_nacimiento_entry = ttk.Entry(self.content_frame)
        self.fecha_nacimiento_entry.pack()

        self.cod_autor_label = ttk.Label(self.content_frame, text="Código de Autor:")
        self.cod_autor_label.pack()
        self.cod_autor_entry = ttk.Entry(self.content_frame)
        self.cod_autor_entry.pack()

        self.pais_label = ttk.Label(self.content_frame, text="País:")
        self.pais_label.pack()
        self.pais_entry = ttk.Entry(self.content_frame)
        self.pais_entry.pack()

        self.editorial_label = ttk.Label(self.content_frame, text="Editorial:")
        self.editorial_label.pack()
        self.editorial_entry = ttk.Entry(self.content_frame)
        self.editorial_entry.pack()

        guardar_button = ttk.Button(self.content_frame, text="Guardar", command=self.guardar_autor)
        guardar_button.pack()

        salir_button = ttk.Button(self.content_frame, text="Cancelar")
        salir_button.pack()

    # Función para editar un autor existente
    def editar_autor(self):
        seleccionado = self.treeview.selection()
        if seleccionado:
            self.indice_autor = int(self.treeview.item(seleccionado)['text'])
            self.editar_autor_fr()
        else:
            self.detalle_label.config(text="Seleccione un autor")

    # Función para mostrar el formulario de edición de autor
    def editar_autor_fr(self):
        self.limpiar_contenido()
        autor = self.listado_autores[self.indice_autor]
        
        self.cod_persona_label = ttk.Label(self.content_frame, text="Código de Persona:")
        self.cod_persona_label.pack()
        self.cod_persona_entry = ttk.Entry(self.content_frame)
        self.cod_persona_entry.pack()
        self.cod_persona_entry.insert(0, self.indice_autor)

        self.nombre_label = ttk.Label(self.content_frame, text="Nombre:")
        self.nombre_label.pack()
        self.nombre_entry = ttk.Entry(self.content_frame)
        self.nombre_entry.pack()
        self.nombre_entry.insert(0, autor.nombre)

        self.apellido_paterno_label = ttk.Label(self.content_frame, text="Apellido Paterno:")
        self.apellido_paterno_label.pack()
        self.apellido_paterno_entry = ttk.Entry(self.content_frame)
        self.apellido_paterno_entry.pack()
        self.apellido_paterno_entry.insert(0, autor.apellido_paterno)

        self.apellido_materno_label = ttk.Label(self.content_frame, text="Apellido Materno:")
        self.apellido_materno_label.pack()
        self.apellido_materno_entry = ttk.Entry(self.content_frame)
        self.apellido_materno_entry.pack()
        self.apellido_materno_entry.insert(0, autor.apellido_materno)

        self.fecha_nacimiento_label = ttk.Label(self.content_frame, text="Fecha de Nacimiento:")
        self.fecha_nacimiento_label.pack()
        self.fecha_nacimiento_entry = ttk.Entry(self.content_frame)
        self.fecha_nacimiento_entry.pack()
        self.fecha_nacimiento_entry.insert(0, autor.fecha_nacimiento)

        self.cod_autor_label = ttk.Label(self.content_frame, text="Código de Autor:")
        self.cod_autor_label.pack()
        self.cod_autor_entry = ttk.Entry(self.content_frame)
        self.cod_autor_entry.pack()
        self.cod_autor_entry.insert(0, autor.cod_autor)

        self.pais_label = ttk.Label(self.content_frame, text="País:")
        self.pais_label.pack()
        self.pais_entry = ttk.Entry(self.content_frame)
        self.pais_entry.pack()
        self.pais_entry.insert(0, autor.pais)

        self.editorial_label = ttk.Label(self.content_frame, text="Editorial:")
        self.editorial_label.pack()
        self.editorial_entry = ttk.Entry(self.content_frame)
        self.editorial_entry.pack()
        self.editorial_entry.insert(0, autor.editorial)

        editar_button = ttk.Button(self.content_frame, text="Guardar", command=self.editar_autor)
        editar_button.pack()

        salir_button = ttk.Button(self.content_frame, text="Cancelar")
        salir_button.pack()

    # Función para guardar un nuevo autor o actualizar uno existente
    def guardar_autor(self):
        cod_persona = self.cod_persona_entry.get()
        nombre = self.nombre_entry.get()
        apellido_paterno = self.apellido_paterno_entry.get()
        apellido_materno = self.apellido_materno_entry.get()
        fecha_nacimiento = self.fecha_nacimiento_entry.get()
        cod_autor = self.cod_autor_entry.get()
        pais = self.pais_entry.get()
        editorial = self.editorial_entry.get()

        # Llama a la función registrar_autor
        reg = self.negocio_autor.registrar_autor(cod_persona, nombre, apellido_paterno, apellido_materno, fecha_nacimiento, cod_autor, pais, editorial)
        reg = self.negocio_autor.guardar_autores()
        print(f"guardado en el excel {reg}")

        # Actualiza la lista de autores
        self.listado_autores = self.negocio_autor.obtener_autores()

        # Muestra el contenido de la opción "Autores"
        self.mostrar_contenido_opcion_autor()

    # Función para editar un registro de autor
    def editar_registro_autor(self):
        cod_persona = self.cod_persona_entry.get()
        nombre = self.nombre_entry.get()
        apellido_paterno = self.apellido_paterno_entry.get()
        apellido_materno = self.apellido_materno_entry.get()
        fecha_nacimiento = self.fecha_nacimiento_entry.get()
        cod_autor = self.cod_autor_entry.get()
        pais = self.pais_entry.get()
        editorial = self.editorial_entry.get()
        print(f'{nombre}, {apellido_paterno}, {apellido_materno}, {fecha_nacimiento}, {cod_autor}, {pais}, {editorial}')

        reg = self.negocio_autor.editar_autor(cod_persona, nombre, apellido_paterno, apellido_materno, fecha_nacimiento, cod_autor, pais, editorial)
        print(f"editado en el excel {reg}")
        self.listado_autores = self.negocio_autor.obtener_autores()
        self.mostrar_contenido_opcion_autor()

    # Función para eliminar un autor
    def eliminar_autor(self):
        seleccionado = self.treeview.selection()
        if seleccionado:
            indice = int(self.treeview.item(seleccionado)['text'])
            mensaje = self.negocio_autor.eliminar_autor(indice)
            self.detalle_label.config(text=mensaje)
            self.mostrar_contenido_opcion_autor()
        else:
            self.detalle_label.config(text="Seleccione un autor")

# CONTENIDO LIBRO
    # Función para mostrar el contenido de la opción "Libros"
    def mostrar_contenido_opcion_libro(self):
        self.limpiar_contenido()# Limpia el contenido anterior
        # Crea un objeto Treeview para mostrar datos
        self.treeview = ttk.Treeview(self.content_frame)
        self.treeview.pack(fill="both", expand=True)

        # Configuración de columnas y encabezados del Treeview
        self.treeview["columns"] = ("Código Libro", "Título", "Año de Publicación", "Tomo")
        self.treeview.column("#0", width=50)
        self.treeview.column("Código Libro", width=100)
        self.treeview.column("Título", width=200)
        self.treeview.column("Año de Publicación", width=100)
        self.treeview.column("Tomo", width=100)

        self.treeview.heading("#0", text="Índice")
        self.treeview.heading("Código Libro", text="Código Libro")
        self.treeview.heading("Título", text="Título")
        self.treeview.heading("Año de Publicación", text="Año de Publicación")
        self.treeview.heading("Tomo", text="Tomo")

        # Obtención de datos de libros y llenado del Treeview
        libros = self.negocio_libro.obtener_libros()

        for i, libro in enumerate(libros):
            self.treeview.insert("", "end", text=i, values=(libro.get_codigo_libro(), libro.get_titulo(), libro.get_año(), libro.get_tomo()))

        # Creación de botones y etiquetas
        detalle_button = ttk.Button(self.content_frame, text="Mostrar Detalle", command=self.mostrar_detalle_libro)
        detalle_button.pack(pady=10)

        nuevo_libro_button = ttk.Button(self.content_frame, text="Nuevo Registro", command=self.nuevo_libro)
        nuevo_libro_button.pack(pady=10)

        editar_libro_button = ttk.Button(self.content_frame, text="Editar Registro", command=self.editar_libro)
        editar_libro_button.pack(pady=10)

        eliminar_libro_button = ttk.Button(self.content_frame, text="Eliminar Registro", command=self.eliminar_libro)
        eliminar_libro_button.pack(pady=10)

        self.detalle_label = ttk.Label(self.content_frame, text="")
        self.detalle_label.pack(padx=20, pady=20)

    # Función para mostrar el detalle de un libro seleccionado
    def mostrar_detalle_libro(self):
        seleccionado = self.treeview.selection()
        if seleccionado:
            indice = int(self.treeview.item(seleccionado)['text'])
            libro = self.negocio_libro.obtener_libros()[indice]
            self.detalle_label.config(text=f"Código Libro: {libro.get_codigo_libro()}\nTítulo: {libro.get_titulo()}\nAño de Publicación: {libro.get_año()}\nTomo: {libro.get_tomo()}")
        else:
            self.detalle_label.config(text="Seleccione un libro")

    # Función para crear un nuevo registro de libro
    def nuevo_libro(self):
        self.limpiar_contenido()
        # Etiquetas y campos de entrada
        self.codigo_libro_label = ttk.Label(self.content_frame, text="Código de Libro:")
        self.codigo_libro_label.pack()
        self.codigo_libro_entry = ttk.Entry(self.content_frame)
        self.codigo_libro_entry.pack()

        self.titulo_label = ttk.Label(self.content_frame, text="Título:")
        self.titulo_label.pack()
        self.titulo_entry = ttk.Entry(self.content_frame)
        self.titulo_entry.pack()

        self.año_publicacion_label = ttk.Label(self.content_frame, text="Año de Publicación:")
        self.año_publicacion_label.pack()
        self.año_publicacion_entry = ttk.Entry(self.content_frame)
        self.año_publicacion_entry.pack()

        self.tomo_label = ttk.Label(self.content_frame, text="Tomo:")
        self.tomo_label.pack()
        self.tomo_entry = ttk.Entry(self.content_frame)
        self.tomo_entry.pack()

        guardar_button = ttk.Button(self.content_frame, text="Guardar", command=self.guardar_libro)
        guardar_button.pack()

        salir_button = ttk.Button(self.content_frame, text="Cancelar")
        salir_button.pack()

    # Función para editar un registro de libro
    def editar_libro(self):
        seleccionado = self.treeview.selection()
        if seleccionado:
            self.indice_libro = int(self.treeview.item(seleccionado)['text'])
            self.editar_libro_fr()
        else:
            self.detalle_label.config(text="Seleccione un libro")

    # Función para mostrar el formulario de edición de libro
    def editar_libro_fr(self):
        self.limpiar_contenido()
        libro = self.listado_libros[self.indice_libro]

        self.codigo_libro_label = ttk.Label(self.content_frame, text="Código de Libro:")
        self.codigo_libro_label.pack()
        self.codigo_libro_entry = ttk.Entry(self.content_frame)
        self.codigo_libro_entry.pack()
        self.codigo_libro_entry.insert(0, libro.codigo_libro)

        self.titulo_label = ttk.Label(self.content_frame, text="Título:")
        self.titulo_label.pack()
        self.titulo_entry = ttk.Entry(self.content_frame)
        self.titulo_entry.pack()
        self.titulo_entry.insert(0, libro.titulo)

        self.año_publicacion_label = ttk.Label(self.content_frame, text="Año de Publicación:")
        self.año_publicacion_label.pack()
        self.año_publicacion_entry = ttk.Entry(self.content_frame)
        self.año_publicacion_entry.pack()
        self.año_publicacion_entry.insert(0, libro.año_publicacion)

        self.tomo_label = ttk.Label(self.content_frame, text="Tomo:")
        self.tomo_label.pack()
        self.tomo_entry = ttk.Entry(self.content_frame)
        self.tomo_entry.pack()
        self.tomo_entry.insert(0, libro.tomo)

        editar_button = ttk.Button(self.content_frame, text="Guardar", command=self.editar_registro_libro)
        editar_button.pack()

        salir_button = ttk.Button(self.content_frame, text="Cancelar")
        salir_button.pack()

    # Función para guardar un nuevo libro
    def guardar_libro(self):
        codigo_libro = self.codigo_libro_entry.get()
        titulo = self.titulo_entry.get()
        año_publicacion = self.año_publicacion_entry.get()
        tomo = self.tomo_entry.get()

        # Llama a la función registrar_libro
        reg = self.negocio_libro.registrar_libro(codigo_libro, titulo, año_publicacion, tomo)
        reg = self.negocio_libro.guardar_libros()
        print(f"guardado en el excel {reg}")
        # Actualiza la lista de libros
        self.listado_libros = self.negocio_libro.obtener_libros()

        # Muestra el contenido de la opción "Libros"
        self.mostrar_contenido_opcion_libro()

    # Función para editar un registro de libro existente
    def editar_registro_libro(self):
        codigo_libro = self.codigo_libro_entry.get()
        titulo = self.titulo_entry.get()
        año_publicacion = self.año_publicacion_entry.get()
        tomo = self.tomo_entry.get()
        print(f'{codigo_libro}, {titulo}, {año_publicacion}, {tomo}')

        reg = self.negocio_libro.editar_libro(codigo_libro, titulo, año_publicacion, tomo)
        print(f"editado en el excel {reg}")
        self.listado_libros = self.negocio_libro.obtener_libros()
        self.mostrar_contenido_opcion_libro()

    # Función para eliminar un registro de libro
    def eliminar_libro(self):
        seleccionado = self.treeview.selection()
        if seleccionado:
            indice = int(self.treeview.item(seleccionado)['text'])
            mensaje = self.negocio_libro.eliminar_libro(indice)
            self.detalle_label.config(text=mensaje)
            self.mostrar_contenido_opcion_libro()
        else:
            self.detalle_label.config(text="Seleccione un libro")

# CONTENIDO CATEGORÍA
    # Función para mostrar el contenido de la opción "Categorías"
    def mostrar_contenido_opcion_categoria(self):
        self.limpiar_contenido()# Limpia el contenido anterior
        # Crea un objeto Treeview para mostrar datos
        self.treeview = ttk.Treeview(self.content_frame)
        self.treeview.pack(fill="both", expand=True)

        # Configuración de columnas y encabezados del Treeview
        self.treeview["columns"] = ("Código Categoría", "Categoría")
        self.treeview.column("#0", width=50)
        self.treeview.column("Código Categoría", width=100)
        self.treeview.column("Categoría", width=200)

        self.treeview.heading("#0", text="Índice")
        self.treeview.heading("Código Categoría", text="Código Categoría")
        self.treeview.heading("Categoría", text="Categoría")

        # Obtención de datos de categorías y llenado del Treeview
        categorias = self.negocio_categoria.obtener_categorias()

        for i, categoria in enumerate(categorias):
            self.treeview.insert("", "end", text=i, values=(categoria.get_cod_categoria(), categoria.get_categoria()))

        # Creación de botones y etiquetas
        detalle_button = ttk.Button(self.content_frame, text="Mostrar Detalle", command=self.mostrar_detalle_categoria)
        detalle_button.pack(pady=10)

        nueva_categoria_button = ttk.Button(self.content_frame, text="Nueva Categoría", command=self.nueva_categoria)
        nueva_categoria_button.pack(pady=10)

        editar_categoria_button = ttk.Button(self.content_frame, text="Editar Categoría", command=self.editar_categoria)
        editar_categoria_button.pack(pady=10)

        eliminar_categoria_button = ttk.Button(self.content_frame, text="Eliminar Categoría", command=self.eliminar_categoria)
        eliminar_categoria_button.pack(pady=10)

    # Función para mostrar el detalle de una categoría seleccionad
    def mostrar_detalle_categoria(self):
        seleccionado = self.treeview.selection()
        if seleccionado:
            indice = int(self.treeview.item(seleccionado)['text'])
            categoria = self.negocio_categoria.obtener_categorias()[indice]
            self.detalle_label.config(text=f"Código Categoría: {categoria.get_cod_categoria()}\nCategoría: {categoria.get_categoria()}")
        else:
            self.detalle_label.config(text="Seleccione una categoría")

    # Función para agregar una nueva categoría
    def nueva_categoria(self):
        self.limpiar_contenido()
        # Etiquetas y campos de entrada
        self.cod_categoria_label = ttk.Label(self.content_frame, text="Código de Categoría:")
        self.cod_categoria_label.pack()
        self.cod_categoria_entry = ttk.Entry(self.content_frame)
        self.cod_categoria_entry.pack()

        self.categoria_label = ttk.Label(self.content_frame, text="Categoría:")
        self.categoria_label.pack()
        self.categoria_entry = ttk.Entry(self.content_frame)
        self.categoria_entry.pack()

        guardar_button = ttk.Button(self.content_frame, text="Guardar", command=self.guardar_categoria)
        guardar_button.pack()

        salir_button = ttk.Button(self.content_frame, text="Cancelar")
        salir_button.pack()

    # Función para editar una categoría
    def editar_categoria(self):
        seleccionado = self.treeview.selection()
        if seleccionado:
            self.indice_categoria = int(self.treeview.item(seleccionado)['text'])
            self.editar_categoria_fr()
        else:
            self.detalle_label.config(text="Seleccione una categoría")
    
    # Función para mostrar el formulario de edición de categoría
    def editar_categoria_fr(self):
        self.limpiar_contenido()
        categoria = self.listado_categorias[self.indice_categoria]

        self.cod_categoria_label = ttk.Label(self.content_frame, text="Código de Categoría:")
        self.cod_categoria_label.pack()
        self.cod_categoria_entry = ttk.Entry(self.content_frame)
        self.cod_categoria_entry.pack()
        self.cod_categoria_entry.insert(0, categoria.cod_categoria)

        self.categoria_label = ttk.Label(self.content_frame, text="Categoría:")
        self.categoria_label.pack()
        self.categoria_entry = ttk.Entry(self.content_frame)
        self.categoria_entry.pack()
        self.categoria_entry.insert(0, categoria.categoria)

        editar_button = ttk.Button(self.content_frame, text="Guardar", command=self.editar_registro_categoria)
        editar_button.pack()

        salir_button = ttk.Button(self.content_frame, text="Cancelar")
        salir_button.pack()

    # Función para guardar una nueva categoría
    def guardar_categoria(self):
        cod_categoria = self.cod_categoria_entry.get()
        categoria = self.categoria_entry.get()

        # Llama a la función registrar_categoria
        reg = self.negocio_categoria.registrar_categoria(cod_categoria, categoria)
        reg = self.negocio_categoria.guardar_categorias()
        print(f"guardado en el excel {reg}")
        # Actualiza la lista de categorías
        self.listado_categorias = self.negocio_categoria.obtener_categorias()

        # Muestra el contenido de la opción "Categorías"
        self.mostrar_contenido_opcion_categoria()

    # Función para editar una categoría existente
    def editar_registro_categoria(self):
        cod_categoria = self.cod_categoria_entry.get()
        categoria = self.categoria_entry.get()
        print(f'{cod_categoria}, {categoria}')

        reg = self.negocio_categoria.editar_categoria(cod_categoria, categoria)
        print(f"editado en el excel {reg}")
        self.listado_categorias = self.negocio_categoria.obtener_categorias()
        self.mostrar_contenido_opcion_categoria()

    # Función para eliminar una categoría
    def eliminar_categoria(self):
        seleccionado = self.treeview.selection()
        if seleccionado:
            indice = int(self.treeview.item(seleccionado)['text'])
            mensaje = self.negocio_categoria.eliminar_categoria(indice)
            self.detalle_label.config(text=mensaje)
            self.mostrar_contenido_opcion_categoria()
        else:
            self.detalle_label.config(text="Seleccione una categoría")

    # Limpiar el contenido actual
    def limpiar_contenido(self):
        for widget in self.content_frame.winfo_children():
            widget.destroy()
        self.treeview = None
        self.detalle_label = ttk.Label(self.content_frame, text="")
        self.detalle_label.pack(padx=10, pady=10, fill="both", expand=True)


# Crear la ventana principal
root = tk.Tk()
app = MainMenuApp(root)
root.mainloop()