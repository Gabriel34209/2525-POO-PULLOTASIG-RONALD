# --- Sistema de Gestión de Biblioteca ---

class Libro:
    """
    Representa un libro en el sistema de la biblioteca.
    """
    def __init__(self, titulo, autor, isbn, disponible=True):
        """
        Constructor de la clase Libro.

        Args:
            titulo (str): El título del libro.
            autor (str): El autor del libro.
            isbn (str): El ISBN (International Standard Book Number) único del libro.
            disponible (bool): True si el libro está disponible para préstamo, False en caso contrario.
        """
        self.titulo = titulo
        self.autor = autor
        self.isbn = isbn
        self.disponible = disponible

    def __str__(self):
        """
        Devuelve una representación en cadena del objeto Libro.
        """
        estado = "Disponible" if self.disponible else "Prestado"
        return f"Título: {self.titulo}, Autor: {self.autor}, ISBN: {self.isbn}, Estado: {estado}"

    def prestar(self):
        """
        Marca el libro como prestado si está disponible.
        """
        if self.disponible:
            self.disponible = False
            print(f"'{self.titulo}' ha sido prestado.")
        else:
            print(f"'{self.titulo}' no está disponible para préstamo.")

    def devolver(self):
        """
        Marca el libro como disponible si estaba prestado.
        """
        if not self.disponible:
            self.disponible = True
            print(f"'{self.titulo}' ha sido devuelto.")
        else:
            print(f"'{self.titulo}' ya estaba disponible.")


class Usuario:
    """
    Representa un usuario de la biblioteca.
    """
    def __init__(self, nombre, id_usuario):
        """
        Constructor de la clase Usuario.

        Args:
            nombre (str): El nombre del usuario.
            id_usuario (str): Un identificador único para el usuario.
            libros_prestados (list): Una lista de objetos Libro que el usuario ha prestado.
        """
        self.nombre = nombre
        self.id_usuario = id_usuario
        self.libros_prestados = []

    def __str__(self):
        """
        Devuelve una representación en cadena del objeto Usuario.
        """
        return f"Usuario: {self.nombre}, ID: {self.id_usuario}, Libros prestados: {len(self.libros_prestados)}"

    def tomar_prestamo(self, libro):
        """
        Permite al usuario tomar prestado un libro si está disponible.

        Args:
            libro (Libro): El objeto Libro que el usuario desea prestar.
        """
        if libro.disponible:
            libro.prestar()
            self.libros_prestados.append(libro)
            print(f"{self.nombre} ha tomado prestado '{libro.titulo}'.")
        else:
            print(f"Lo siento, '{libro.titulo}' no está disponible para préstamo en este momento.")

    def devolver_libro(self, libro):
        """
        Permite al usuario devolver un libro.

        Args:
            libro (Libro): El objeto Libro que el usuario desea devolver.
        """
        if libro in self.libros_prestados:
            libro.devolver()
            self.libros_prestados.remove(libro)
            print(f"{self.nombre} ha devuelto '{libro.titulo}'.")
        else:
            print(f"{self.nombre} no tiene prestado '{libro.titulo}'.")


class Biblioteca:
    """
    Representa el sistema de gestión de la biblioteca.
    Mantiene un registro de los libros y usuarios.
    """
    def __init__(self, nombre):
        """
        Constructor de la clase Biblioteca.

        Args:
            nombre (str): El nombre de la biblioteca.
            catalogo (list): Una lista de objetos Libro disponibles en la biblioteca.
            miembros (list): Una lista de objetos Usuario registrados en la biblioteca.
        """
        self.nombre = nombre
        self.catalogo = []
        self.miembros = []

    def agregar_libro(self, libro):
        """
        Agrega un libro al catálogo de la biblioteca.

        Args:
            libro (Libro): El objeto Libro a agregar.
        """
        self.catalogo.append(libro)
        print(f"'{libro.titulo}' agregado al catálogo de la biblioteca.")

    def registrar_usuario(self, usuario):
        """
        Registra un nuevo usuario en la biblioteca.

        Args:
            usuario (Usuario): El objeto Usuario a registrar.
        """
        self.miembros.append(usuario)
        print(f"Usuario '{usuario.nombre}' registrado en la biblioteca.")

    def buscar_libro(self, consulta, tipo="titulo"):
        """
        Busca un libro en el catálogo de la biblioteca por título o autor.

        Args:
            consulta (str): El texto de búsqueda.
            tipo (str): El tipo de búsqueda ('titulo' o 'autor').

        Returns:
            list: Una lista de objetos Libro que coinciden con la consulta.
        """
        resultados = []
        for libro in self.catalogo:
            if tipo == "titulo" and consulta.lower() in libro.titulo.lower():
                resultados.append(libro)
            elif tipo == "autor" and consulta.lower() in libro.autor.lower():
                resultados.append(libro)
        return resultados

    def mostrar_catalogo(self):
        """
        Muestra todos los libros en el catálogo de la biblioteca.
        """
        if not self.catalogo:
            print("El catálogo de la biblioteca está vacío.")
            return
        print("\n--- Catálogo de la Biblioteca ---")
        for libro in self.catalogo:
            print(libro)
        print("---------------------------------")

    def mostrar_miembros(self):
        """
        Muestra todos los usuarios registrados en la biblioteca.
        """
        if not self.miembros:
            print("No hay miembros registrados en la biblioteca.")
            return
        print("\n--- Miembros de la Biblioteca ---")
        for miembro in self.miembros:
            print(miembro)
        print("---------------------------------")


# --- Demostración del Sistema de Gestión de Biblioteca ---

if __name__ == "__main__":
    # 1. Crear una instancia de la biblioteca
    mi_biblioteca = Biblioteca("Biblioteca Central de Quito")

    # 2. Crear instancias de libros
    libro1 = Libro("Cien Años de Soledad", "Gabriel García Márquez", "978-0307474728")
    libro2 = Libro("Don Quijote de la Mancha", "Miguel de Cervantes", "978-8424102928")
    libro3 = Libro("1984", "George Orwell", "978-0451524935")
    libro4 = Libro("Orgullo y Prejuicio", "Jane Austen", "978-0141439518")

    # 3. Agregar libros a la biblioteca
    mi_biblioteca.agregar_libro(libro1)
    mi_biblioteca.agregar_libro(libro2)
    mi_biblioteca.agregar_libro(libro3)
    mi_biblioteca.agregar_libro(libro4)

    # 4. Crear instancias de usuarios
    usuario1 = Usuario("Ana García", "U001")
    usuario2 = Usuario("Pedro Martínez", "U002")

    # 5. Registrar usuarios en la biblioteca
    mi_biblioteca.registrar_usuario(usuario1)
    mi_biblioteca.registrar_usuario(usuario2)

    # 6. Mostrar el catálogo inicial y los miembros
    mi_biblioteca.mostrar_catalogo()
    mi_biblioteca.mostrar_miembros()

    # 7. Interacciones de préstamo y devolución
    print("\n--- Interacciones de Préstamo y Devolución ---")
    usuario1.tomar_prestamo(libro1)
    usuario1.tomar_prestamo(libro3)
    usuario2.tomar_prestamo(libro2)

    # Intentar prestar un libro no disponible
    usuario2.tomar_prestamo(libro1)

    mi_biblioteca.mostrar_catalogo() # Ver el estado de los libros después de los préstamos

    print(usuario1)
    print(usuario2)

    usuario1.devolver_libro(libro1)
    usuario2.devolver_libro(libro2)

    # Intentar devolver un libro que no se tiene prestado
    usuario1.devolver_libro(libro4)

    mi_biblioteca.mostrar_catalogo() # Ver el estado de los libros después de las devoluciones
    print(usuario1)
    print(usuario2)

    # 8. Búsqueda de libros
    print("\n--- Búsquedas en la Biblioteca ---")
    resultados_titulo = mi_biblioteca.buscar_libro("1984", tipo="titulo")
    print("\nResultados de búsqueda por título '1984':")
    for libro in resultados_titulo:
        print(libro)

    resultados_autor = mi_biblioteca.buscar_libro("Cervantes", tipo="autor")
    print("\nResultados de búsqueda por autor 'Cervantes':")
    for libro in resultados_autor:
        print(libro)

    resultados_nada = mi_biblioteca.buscar_libro("No Existe", tipo="titulo")
    print("\nResultados de búsqueda por título 'No Existe':")
    if not resultados_nada:
        print("No se encontraron libros.")