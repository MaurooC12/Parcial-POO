# PARCIAL POO: Sistema de Gestión para Biblioteca Universitaria

## 📌 Descripción
Implemententación de un simulador de operaciones básicas de una biblioteca universitaria, diseñando e implementando las clases y conceptos vistos en clase (encapsulamiento, instanciación, atributos, objetos, etc.)

---

## Clases y Métodos

### 📚 Clase Libro
**Atributos:**
  - tituloLibro: Título del libro (público).
  - categoriaLibro: Categoría del libro (público).
**Métodos:**
  - verDetalles(): Retorna la información completa del libro.
  - verTitulo(): Retorna solo el título del libro.

---

### 👤 Clase Usuario
**Atributos:**
  - _nombreUsuario: Nombre del usuario (protegido).
  - carreraUsuario: Carrera a la que pertenece el usuario (público).
  - __libroDeInteres: Libro de interés del usuario (privado con name mangling).
**Encapsulación con propiedades:**
  - @property libroDeInteres: Permite acceder al libro de interés.
  - @libroDeInteres.setter: Permite actualizar el libro de interés de manera controlada.
**Métodos:**
  - verDetalles(): Retorna la información básica del usuario.

---

### 📖 Clase Libreria
**Atributos:**
  - _categorias: Categorías disponibles en la librería.
  - _libros: Lista de libros registrados.
  - _usuarios: Lista de usuarios registrados.
**Métodos:**
  - agregarLibro(titulo, categoria): Añade un libro si la categoría existe.
  - agregarUsuario(nombre, carrera, libroDeInteres): Registra un nuevo usuario.
  - mostrarLibros(): Muestra todos los libros registrados.
  - mostrarLibrosPorCategoria(categoria): Filtra libros según la categoría.
  - mostrarUsuarios(): Muestra todos los usuarios registrados.

---

## 📄 Tabla de Requerimientos

<img width="593" height="123" alt="image" src="https://github.com/user-attachments/assets/0b8af950-99f9-4985-b21c-2ce04c16b96b" />


---

## 🧠 Justificación del Diseño
El diseño inicial fue considerar implementaciones básicas pero necesarias para que la biblioteca fuese funcionan, se intenta tener una división y organización en el código, adicional de implementación de tabulaciones y saltos de línea para organizar las impresiones en pantalla

---

## ▶️ Ejecución
Para ejecutar el sistema, abre la terminal en la carpeta del proyecto y corre:

bash
python biblioteca.py
