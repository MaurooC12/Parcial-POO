# Author: Mauricio Cepeda Villanueva
# Curso: Programación Orientada a Objetos
# Fecha: 2024-06-20
# Sistema de gestión para una biblioteca universitaria. 
class Libro:
    def __init__(self, tituloLibro, categoriaLibro):
        self.tituloLibro = tituloLibro
        self.categoriaLibro = categoriaLibro

    def verDetalles(self):
        return f'\tTítulo: {self.tituloLibro} \n\tCategoría: {self.categoriaLibro}'
    def verTitulo(self):
        return f'\tTítulo: {self.tituloLibro}'
    
class Usuario:
    def __init__(self, nombreUsuario, carreraUsuario, libroDeInteres):
        self._nombreUsuario = nombreUsuario
        self.carreraUsuario = carreraUsuario
        self.__libroDeInteres = libroDeInteres

    @property
    def libroDeInteres(self):
        return self.__libroDeInteres

    @libroDeInteres.setter
    def libroDeInteres(self, nuevoLibro):
        self.__libroDeInteres = nuevoLibro

    def verDetalles(self):
        return f'\tUsuario: {self._nombreUsuario} \n\tCarrera: {self.carreraUsuario}'


class Libreria:
    def __init__(self):
        self._categorias = ["Ciencias", "Ficcion", "Historia"]
        self._libros = []
        self._usuarios = []

    def agregarLibro(self, titulo, categoria):
        if categoria not in self._categorias:
            print(f"Categoría '{categoria}' no se encuentra aún. Las categorías válidas por ahora son: {self._categorias}")
            return
        nuevoLibro = Libro(titulo, categoria)
        self._libros.append(nuevoLibro)
        print("\n - - - -\nLIBRO AÑADIDO CON ÉXITO! \n - - - -\n", nuevoLibro.verDetalles())

    def agregarUsuario(self, nombreUsuario, carreraUsuario, libroDeInteres):
        nuevoUsuario = Usuario(nombreUsuario, carreraUsuario, libroDeInteres)
        self._usuarios.append(nuevoUsuario)
        print("\n - - - -\nUSER REGISTRADO CON ÉXITO! \n - - - -\n", nuevoUsuario.verDetalles())

    def mostrarLibros(self):
        if not self._libros:
            print("No hay libros registrados.")
        for libro in self._libros:
            print(libro.verDetalles())

    def mostrarLibrosPorCategoria(self, categoria):
        encontrados = [libro for libro in self._libros if libro.categoriaLibro == categoria]
        if not encontrados:
            print(f"No hay libros en la categoría '{categoria}'.")
        for libro in encontrados:
            print(libro.verTitulo())

    def mostrarUsuarios(self):
        if not self._usuarios:
            print("No hay usuarios registrados.")
        for usuario in self._usuarios:
            print(usuario.verDetalles())


if __name__ == "__main__":
    libreria = Libreria()
    while True:
        print("\nMenú de Biblioteca Universitaria")
        print("1. Agregar libro")
        print("2. Buscar libros por categoría")
        print("3. Mostrar todos los libros")
        print("4. Crear usuario")
        print("5. Mostrar usuarios")
        print("6. Salir")

        opcion = input("Selecciona una opción (1 al 6): ")

        match opcion:
            case "1":
                titulo = input("Título del libro: ")
                print("Categorías disponibles: Ciencias, Ficcion, Historia")
                categoria = input("Categoría del libro: ")
                libreria.agregarLibro(titulo, categoria)

            case "2":
                categoria = input("Ingresa la categoría a buscar: ")
                print(f"\nLibros en la categoría '{categoria}':")
                libreria.mostrarLibrosPorCategoria(categoria)

            case "3":
                print("\nLibros en la librería:")
                libreria.mostrarLibros()

            case "4":
                nombre = input("Nombre del usuario: ")
                carrera = input("Carrera del usuario: ")
                libroInteres = input("Libro de interés del usuario: ")
                libreria.agregarUsuario(nombre, carrera, libroInteres)

            case "5":
                print("\nUsuarios registrados:")
                libreria.mostrarUsuarios()

            case "6":
                print("Baiss")
                break