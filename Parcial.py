# Autor: Mauricio Cepeda Villanueva
# Curso: Programación Orientada a Objetos
# Fecha: 2024-06-20
# Sistema de gestión para una biblioteca universitaria (versión modular sin herencia)

class Libro:
    def __init__(self, tituloLibro, categoriaLibro):
        self.tituloLibro = tituloLibro
        self.categoriaLibro = categoriaLibro

    def verDetalles(self):
        return f'\tTítulo: {self.tituloLibro} \n\tCategoría: {self.categoriaLibro}'

    def verTitulo(self):
        return self.tituloLibro


class Usuario:
    def __init__(self, nombreUsuario, carreraUsuario, libroDeInteres):
        self.nombreUsuario = nombreUsuario
        self.carreraUsuario = carreraUsuario
        self.libroDeInteres = libroDeInteres

    def verDetalles(self):
        return f'\tUsuario: {self.nombreUsuario} \n\tCarrera: {self.carreraUsuario}'


class Libreria:
    def __init__(self):
        self._categorias = ["Ciencias", "Ficcion", "Historia"]
        self._libros = []
        self._usuarios = []

    def agregarLibro(self, titulo, categoria):
        if categoria not in self._categorias:
            print(f"Categoría '{categoria}' no se encuentra aún. Categorías válidas: {self._categorias}")
            return
        nuevoLibro = Libro(titulo, categoria)
        self._libros.append(nuevoLibro)
        print("\n - - - -\nLIBRO AÑADIDO CON ÉXITO!\n - - - -\n", nuevoLibro.verDetalles())

    def mostrarLibros(self):
        if not self._libros:
            print("No hay libros registrados.")
        else:
            for libro in self._libros:
                print(libro.verDetalles())

    def mostrarLibrosPorCategoria(self, categoria):
        encontrados = [libro for libro in self._libros if libro.categoriaLibro == categoria]
        if not encontrados:
            print(f"No hay libros en la categoría '{categoria}'.")
        else:
            for libro in encontrados:
                print("Título:", libro.verTitulo())

    def agregarUsuario(self, nombreUsuario, carreraUsuario, libroDeInteres):
        nuevoUsuario = Usuario(nombreUsuario, carreraUsuario, libroDeInteres)
        self._usuarios.append(nuevoUsuario)
        print("\n - - - -\nUSUARIO REGISTRADO CON ÉXITO!\n - - - -\n", nuevoUsuario.verDetalles())

    def mostrarUsuarios(self):
        if not self._usuarios:
            print("No hay usuarios registrados.")
        else:
            for usuario in self._usuarios:
                print(usuario.verDetalles())

    def mostrarMenu(self):
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
                    self.agregarLibro(titulo, categoria)

                case "2":
                    categoria = input("Ingresa la categoría a buscar: ")
                    print(f"\nLibros en la categoría '{categoria}':")
                    self.mostrarLibrosPorCategoria(categoria)

                case "3":
                    print("\nLibros en la librería:")
                    self.mostrarLibros()

                case "4":
                    nombre = input("Nombre del usuario: ")
                    carrera = input("Carrera del usuario: ")
                    libroInteres = input("Libro de interés del usuario: ")
                    self.agregarUsuario(nombre, carrera, libroInteres)

                case "5":
                    print("\nUsuarios registrados:")
                    self.mostrarUsuarios()

                case "6":
                    print("¡Hasta luego!")
                    break

                case _:
                    print("Opción no válida. Intenta de nuevo.")

def main():
    libreria = Libreria()
    libreria.mostrarMenu()


if __name__ == "__main__":
    main()
