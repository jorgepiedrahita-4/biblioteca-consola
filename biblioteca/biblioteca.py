"""
Sistema de Gestión de Biblioteca con Árbol Binario de Búsqueda (ABB)

Estructuras:
- Árbol Binario de Búsqueda para libros (organizados por ISBN).
- NodoLibro representa cada libro como un nodo del árbol.

Este sistema permite:
- Crear, editar, eliminar y listar libros en una biblioteca.
"""

class NodoLibro:
    """Clase que representa un nodo de libro en el ABB."""
    def __init__(self, isbn, titulo, autor, anio, disponible=True):
        self.isbn = isbn
        self.titulo = titulo
        self.autor = autor
        self.anio = anio
        self.disponible = disponible
        self.izq = None
        self.der = None

class ArbolLibros:
    """Clase del Árbol Binario de Búsqueda para gestionar libros."""
    def __init__(self):
        self.raiz = None

    def insertar(self, nodo):
        """Inserta un nuevo nodo en el ABB."""
        self.raiz = self._insertar_rec(self.raiz, nodo)

    def _insertar_rec(self, actual, nodo):
        if actual is None:
            return nodo
        if nodo.isbn < actual.isbn:
            actual.izq = self._insertar_rec(actual.izq, nodo)
        elif nodo.isbn > actual.isbn:
            actual.der = self._insertar_rec(actual.der, nodo)
        return actual

    def buscar(self, isbn):
        """Busca un libro por ISBN."""
        return self._buscar_rec(self.raiz, isbn)

    def _buscar_rec(self, actual, isbn):
        if actual is None or actual.isbn == isbn:
            return actual
        if isbn < actual.isbn:
            return self._buscar_rec(actual.izq, isbn)
        else:
            return self._buscar_rec(actual.der, isbn)

    def eliminar(self, isbn):
        """Elimina un libro por ISBN."""
        self.raiz = self._eliminar_rec(self.raiz, isbn)

    def _eliminar_rec(self, actual, isbn):
        if actual is None:
            return None
        if isbn < actual.isbn:
            actual.izq = self._eliminar_rec(actual.izq, isbn)
        elif isbn > actual.isbn:
            actual.der = self._eliminar_rec(actual.der, isbn)
        else:
            # Nodo con solo un hijo o sin hijos
            if actual.izq is None:
                return actual.der
            elif actual.der is None:
                return actual.izq
            # Nodo con dos hijos
            sucesor = self._min_valor(actual.der)
            actual.isbn = sucesor.isbn
            actual.titulo = sucesor.titulo
            actual.autor = sucesor.autor
            actual.anio = sucesor.anio
            actual.disponible = sucesor.disponible
            actual.der = self._eliminar_rec(actual.der, sucesor.isbn)
        return actual

    def _min_valor(self, nodo):
        """Obtiene el nodo con menor ISBN (más a la izquierda)."""
        actual = nodo
        while actual.izq is not None:
            actual = actual.izq
        return actual

    def recorrer_inorden(self):
        """Recorre el árbol en inorden para listar libros."""
        libros = []
        self._inorden_rec(self.raiz, libros)
        return libros

    def _inorden_rec(self, nodo, lista):
        if nodo is not None:
            self._inorden_rec(nodo.izq, lista)
            lista.append(nodo)
            self._inorden_rec(nodo.der, lista)

# Inicialización
biblioteca = ArbolLibros()
# Carga inicial
biblioteca.insertar(NodoLibro("978-0307474278", "1984", "George Orwell", 1949))
biblioteca.insertar(NodoLibro("978-0061120084", "Cien años de soledad", "Gabriel García Márquez", 1967))

# Funciones de interacción
def crear_libro():
    print("\n--- CREAR LIBRO ---")
    isbn = input("ISBN: ").strip()
    if biblioteca.buscar(isbn):
        print(" El libro ya existe.")
        return
    titulo = input("Título: ").strip()
    autor = input("Autor: ").strip()
    anio = input("Año: ").strip()
    nodo = NodoLibro(isbn, titulo, autor, anio)
    biblioteca.insertar(nodo)
    print(f" Libro '{titulo}' registrado.")

def editar_libro():
    print("\n--- EDITAR LIBRO ---")
    isbn = input("ISBN del libro a editar: ").strip()
    nodo = biblioteca.buscar(isbn)
    if nodo:
        print(f"Editando: {nodo.titulo}")
        nodo.titulo = input(f"Nuevo título ({nodo.titulo}): ") or nodo.titulo
        nodo.autor = input(f"Nuevo autor ({nodo.autor}): ") or nodo.autor
        nodo.anio = input(f"Nuevo año ({nodo.anio}): ") or nodo.anio
        print(" Libro actualizado.")
    else:
        print(" Libro no encontrado.")

def eliminar_libro():
    print("\n--- ELIMINAR LIBRO ---")
    isbn = input("ISBN del libro a eliminar: ").strip()
    if biblioteca.buscar(isbn):
        biblioteca.eliminar(isbn)
        print(" Libro eliminado.")
    else:
        print(" Libro no encontrado.")

def listar_libros():
    print("\n--- CATÁLOGO ---")
    libros = biblioteca.recorrer_inorden()
    if not libros:
        print("No hay libros registrados.")
    else:
        for l in libros:
            estado = "Disponible" if l.disponible else "Prestado"
            print(f"ISBN: {l.isbn} | {l.titulo} ({l.anio})")
            print(f"Autor: {l.autor} | Estado: {estado}\n")

def menu():
    while True:
        print("\n=== MENÚ BIBLIOTECA ===")
        print("1. Crear libro")
        print("2. Editar libro")
        print("3. Eliminar libro")
        print("4. Listar libros")
        print("5. Salir")
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            crear_libro()
        elif opcion == "2":
            editar_libro()
        elif opcion == "3":
            eliminar_libro()
        elif opcion == "4":
            listar_libros()
        elif opcion == "5":
            print("¡Hasta luego! ")
            break
        else:
            print(" Opción inválida.")

if __name__ == "__main__":
    menu()
