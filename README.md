# PARCIAL POO: Sistema de Gestión para Biblioteca Universitaria

## Descripción
Implemententación de un simulador de operaciones básicas de una biblioteca universitaria, diseñando e implementando las clases y conceptos vistos en clase (encapsulamiento, instanciación, atributos, objetos, etc.)

---

## Clases y Métodos

### Clase Libro
**Atributos:**
  - tituloLibro: Título del libro (público).
  - categoriaLibro: Categoría del libro (público).

**Métodos:**
  - verDetalles(): Retorna la información completa del libro.
  - verTitulo(): Retorna solo el título del libro.

---

### Clase Usuario
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

### Clase Libreria
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

## Tabla de Requerimientos

### Registro de nuevos libros - 	✅
### Registro de nuevos usuarios	- ✅
### Mínimo 3 categorías por libro -	✅


---

## Justificación del Diseño
El diseño inicial fue considerar implementaciones básicas pero necesarias para que la biblioteca fuese funcionan, se intenta tener una división y organización en el código, adicional de implementación de tabulaciones y saltos de línea para organizar las impresiones en pantalla

---
## Salidas del Sistema
### Menú
<img width="335" height="201" alt="image" src="https://github.com/user-attachments/assets/2d3ef9f5-1a6b-4131-870e-aac23d307144" />

### Interacción opción 1
<img width="516" height="228" alt="image" src="https://github.com/user-attachments/assets/19fc85be-5ae4-49a3-8ab7-e4dd728846c8" />

### Interacción opcion 2
<img width="425" height="125" alt="image" src="https://github.com/user-attachments/assets/87dc6524-968a-472d-aa3f-1e9f4502f370" />

### Interacción opción 3
<img width="392" height="121" alt="image" src="https://github.com/user-attachments/assets/dbf3f95c-5bda-412a-9f69-8a197f728107" />

### Interacción opción 4
<img width="440" height="224" alt="image" src="https://github.com/user-attachments/assets/a680ae88-59ee-4be3-8620-2fbbf5070434" />

### Interacción opción 5
<img width="349" height="127" alt="image" src="https://github.com/user-attachments/assets/2779fbf0-c07f-427b-b40c-e6d1aaebbb78" />

---

## Autor: Andrés Mauricio Cepeda Villanueva
