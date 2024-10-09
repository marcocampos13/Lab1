class Autor:
    def __init__(self, nombre, nacionalidad):
        self.nombre = nombre
        self.nacionalidad = nacionalidad

class Editorial:
    def __init__(self, nombre, ciudad, estado, pais, website):
        self.nombre = nombre
        self.ciudad = ciudad
        self.estado = estado
        self.pais = pais
        self.website = website

class Libro:
    def __init__(self, titulo, autor, editorial, fecha_publicacion, descripcion):
        self.titulo = titulo
        self.autor = autor  # Autor puede ser uno o una lista de autores
        self.editorial = editorial
        self.fecha_publicacion = fecha_publicacion
        self.descripcion = descripcion
        self.nivel_avance = 0  # Porcentaje de avance de lectura
        self.anotaciones = []  # Lista de anotaciones o stickies

    def agregar_anotacion(self, nota):
        self.anotaciones.append(nota)

    def mostrar_anotaciones(self):
        return self.anotaciones

    def actualizar_avance(self, avance):
        if 0 <= avance <= 100:
            self.nivel_avance = avance
        else:
            print("Por favor, ingrese un valor de avance entre 0 y 100.")

    def mostrar_info(self):
        autores = ', '.join([autor.nombre for autor in self.autor])
        return f"'{self.titulo}' por {autores}, publicado por {self.editorial.nombre} en {self.fecha_publicacion}. Descripción: {self.descripcion}"

class Usuario:
    def __init__(self, identificacion, nombre_completo, tipo):
        self.identificacion = identificacion
        self.nombre_completo = nombre_completo
        self.tipo = tipo
        self.libro_actual = None
        self.biblioteca_rapida = []
        self.anotaciones = {}

    def acceder_libro(self, libro):
        if self.libro_actual is None:
            self.libro_actual = libro
            print(f"{self.nombre_completo} ahora tiene acceso a '{libro.titulo}'")
        else:
            print(f"{self.nombre_completo} ya tiene acceso a un libro: '{self.libro_actual.titulo}'")

    def liberar_libro(self):
        if self.libro_actual:
            print(f"{self.nombre_completo} ha liberado '{self.libro_actual.titulo}'")
            self.libro_actual = None

    def agregar_a_biblioteca_rapida(self, libro):
        self.biblioteca_rapida.append(libro)

    def crear_anotacion(self, libro, anotacion):
        if libro in self.biblioteca_rapida or libro == self.libro_actual:
            libro.agregar_anotacion(anotacion)
            self.anotaciones[libro.titulo] = libro.mostrar_anotaciones()
        else:
            print("El libro no está en la biblioteca rápida o no es el libro actual.")

    def mostrar_anotaciones(self, libro):
        if libro.titulo in self.anotaciones:
            return self.anotaciones[libro.titulo]
        else:
            return "No hay anotaciones para este libro."

    def mostrar_biblioteca_rapida(self):
        return [libro.titulo for libro in self.biblioteca_rapida]

# Datos de autores
autor1 = Autor("Gabriel García Márquez", "Colombiano")
autor2 = Autor("J.K. Rowling", "Británica")
autor3 = Autor("George Orwell", "Británico")
autor4 = Autor("Miguel de Cervantes", "Español")
autor5 = Autor("Homer", "Griego")

# Datos de editoriales
editorial1 = Editorial("Penguin Books", "Londres", "Inglaterra", "Reino Unido", "penguin.co.uk")
editorial2 = Editorial("Santillana", "Madrid", "Madrid", "España", "santillana.com")
editorial3 = Editorial("Planeta", "Barcelona", "Cataluña", "España", "planeta.es")

# Crear libros
libro1 = Libro("Cien años de soledad", [autor1], editorial1, "06/1967", "Una obra maestra de realismo mágico.")
libro2 = Libro("Harry Potter y la piedra filosofal", [autor2], editorial1, "07/1997", "Primera entrega de la saga de Harry Potter.")
libro3 = Libro("1984", [autor3], editorial1, "06/1949", "Distopía sobre el control totalitario.")
libro4 = Libro("Don Quijote de la Mancha", [autor4], editorial2, "01/1605", "Una obra clave de la literatura española.")
libro5 = Libro("La Ilíada", [autor5], editorial3, "08/800 A.C.", "Una epopeya clásica griega sobre la guerra de Troya.")

# Crear usuarios
usuario1 = Usuario("123", "Carlos Pérez", "estudiante")
usuario2 = Usuario("456", "Ana Rodríguez", "profesor")

# Agregar libros a la biblioteca rápida de cada usuario
usuario1.agregar_a_biblioteca_rapida(libro1)
usuario1.agregar_a_biblioteca_rapida(libro3)

usuario2.agregar_a_biblioteca_rapida(libro4)
usuario2.agregar_a_biblioteca_rapida(libro5)

# Mostrar la biblioteca rápida de los usuarios
print(f"Biblioteca rápida de {usuario1.nombre_completo}: {usuario1.mostrar_biblioteca_rapida()}")
print(f"Biblioteca rápida de {usuario2.nombre_completo}: {usuario2.mostrar_biblioteca_rapida()}")

# El usuario 1 accede a un libro y agrega una anotación
usuario1.acceder_libro(libro1)
usuario1.crear_anotacion(libro1, "Capítulo 1: Introducción al realismo mágico.")
usuario1.crear_anotacion(libro1, "Capítulo 2: Comienza la historia de la familia Buendía.")

# El usuario 2 accede a otro libro y agrega una anotación
usuario2.acceder_libro(libro4)
usuario2.crear_anotacion(libro4, "Capítulo 1: Don Quijote y Sancho Panza se conocen.")

# Mostrar las anotaciones del usuario 1
print(f"Anotaciones de {usuario1.nombre_completo} en '{libro1.titulo}': {usuario1.mostrar_anotaciones(libro1)}")

# Mostrar las anotaciones del usuario 2
print(f"Anotaciones de {usuario2.nombre_completo} en '{libro4.titulo}': {usuario2.mostrar_anotaciones(libro4)}")
