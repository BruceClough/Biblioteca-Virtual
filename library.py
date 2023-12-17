import json

class Libro:
    def __init__(self, titulo, autor, categoria, estante):
        self.titulo = titulo
        self.autor = autor
        self.categoria = categoria
        self.estante = estante

    def __str__(self):
        return f"Titulo: {self.titulo}, Autor: {self.autor}, Categoria: {self.categoria}, Estante: {self.estante}"

class SistemaClasificacion:
    def __init__(self):
        self.libros = []
        self.cargar_libros()
    
    def guardar_libros(self):
        with open("libros.json", "w") as archivo:
            libros = []
            for libro in self.libros:
                libros.append({
                    "titulo": libro.titulo,
                    "autor": libro.autor,
                    "categoria": libro.categoria,
                    "estante": libro.estante
                })
            json.dump(libros, archivo)
    
    def cargar_libros(self):
        try:
            with open("libros.json", "r") as archivo:
                libros = json.load(archivo)
                for libro in libros:
                    self.libros.append(Libro(libro["titulo"], libro["autor"], libro["categoria"], libro["estante"]))
        except:
            pass
    
    def agregar_libro(self):
        titulo = input("Ingrese el título del libro: ")
        autor = input("Ingrese el autor del libro: ")
        categoria = input("Ingrese la categoria del libro: ")
        estante = input("Ingrese el estante del libro: ")

        libro = Libro(titulo, autor, categoria, estante)
        self.libros.append(libro)
        print(f"Libro {titulo} agregado correctamente")

    def modificar_libro(self):
        titulo = input("Ingrese el título del libro a modificar: ")
        for libro in self.libros:
            if libro.titulo == titulo:
                libro.titulo = input("Ingrese el título del libro: ")
                libro.autor = input("Ingrese el autor del libro: ")
                libro.categoria = input("Ingrese la categoria del libro: ")
                libro.estante = input("Ingrese el estante del libro: ")
                print(f"Libro {titulo} modificado correctamente")
                return
        print("Libro no encontrado")
    
    def eliminar_libro(self):
        titulo = input("Ingrese el título del libro a eliminar: ")
        for libro in self.libros:
            if libro.titulo == titulo:
                self.libros.remove(libro)
                print(f"Libro {titulo} eliminado correctamente")
                return
        print("Libro no encontrado")

    def listar_libros(self):
        for libro in self.libros:
            print(libro)

    def buscar_libro(self):
        titulo = input("Ingrese el título del libro a buscar: ")
        for libro in self.libros:
            if libro.titulo == titulo:
                print(libro)
                return
        print("Libro no encontrado")
    
    def menu(self):
        while True:
            print("1. Agregar libro")
            print("2. Listar libros")
            print("3. Buscar libro")
            print("4. Modificar libro")
            print("5. Eliminar libro")
            print("6. Salir")
            opcion = input("Ingrese una opción: ")

            if opcion == "1":
                self.agregar_libro()
                self.guardar_libros()
            elif opcion == "2":
                self.listar_libros()
            elif opcion == "3":
                self.buscar_libro()
            elif opcion == "4":
                self.modificar_libro()
                self.guardar_libros()
            elif opcion == "5":
                self.eliminar_libro()
                self.guardar_libros()
            elif opcion == "6":
                break
            else:
                print("Opción incorrecta")
                


sistema = SistemaClasificacion()
sistema.menu()