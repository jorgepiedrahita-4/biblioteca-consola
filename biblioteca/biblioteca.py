"""
Sistema de Gestión de Biblioteca
Estructuras:
- Libros: ISBN, título, autor, anio, disponible
"""

# Base de datos simulada
libros = [
    {"isbn": "978-0307474278", "titulo": "1984", "autor": "George Orwell", "anio": 1949, "disponible": True},
    {"isbn": "978-0061120084", "titulo": "Cien años de soledad", "autor": "Gabriel García Márquez", "anio": 1967, "disponible": True}
]

def crear_libro():
    """Agrega un nuevo libro con ISBN."""
    print("\n--- CREAR LIBRO ---")
    isbn = input("ISBN (ej: 978-1234567890): ").strip()
    titulo = input("Título: ").strip()
    autor = input("Autor: ").strip()
    anio = input("Año de publicación: ").strip()
    
    libros.append({
        "isbn": isbn,
        "titulo": titulo,
        "autor": autor,
        "anio": anio,
        "disponible": True
    })
    print(f" Libro '{titulo}' registrado.")

def editar_libro():
    """Modifica un libro por ISBN."""
    print("\n--- EDITAR LIBRO ---")
    isbn = input("ISBN del libro a editar: ").strip()
    for libro in libros:
        if libro["isbn"] == isbn:
            print(f"Editando: {libro['titulo']}")
            libro["titulo"] = input(f"Nuevo título ({libro['titulo']}): ") or libro["titulo"]
            libro["autor"] = input(f"Nuevo autor ({libro['autor']}): ") or libro["autor"]
            libro["anio"] = input(f"Nuevo anio ({libro['anio']}): ") or libro["anio"]
            print(" Libro actualizado.")
            return
    print(" Libro no encontrado.")

def eliminar_libro():
    """Elimina un libro por ISBN."""
    print("\n--- ELIMINAR LIBRO ---")
    isbn = input("ISBN del libro a eliminar: ").strip()
    for libro in libros:
        if libro["isbn"] == isbn:
            libros.remove(libro)
            print(" Libro eliminado.")
            return
    print(" Libro no encontrado.")

def listar_libros():
    """Muestra todos los libros."""
    print("\n--- CATÁLOGO ---")
    if not libros:
        print("No hay libros registrados.")
    else:
        for libro in libros:
            disp = "Disponible" if libro["disponible"] else "Prestado"
            print(f"ISBN: {libro['isbn']} | {libro['titulo']} ({libro['anio']})")
            print(f"Autor: {libro['autor']} | Estado: {disp}\n")

def menu():
    """Menú interactivo."""
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
