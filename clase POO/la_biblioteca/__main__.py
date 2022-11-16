import biblioteca
import libro
import miembro

biblio1 = biblioteca.Biblioteca("Biblioteca Nacional", "7 1429", "4836318")
libro1 = libro.Libro("Harry Potter", "J. K. Rowling", "fantasía")
libro2 = libro.Libro("Farenheit 451", "Ray Bradbury", "ficcion")
libro3 = libro.Libro("La Odisea", "Anónimo", "historico")
libro4 = libro.Libro("It", "Sthepen King", "terror")
libro5 = libro.Libro("Drácula", "Bram Stoker", "terror")
libro6 = libro.Libro("Frankenstein", "Mary Shelley", "terror")
libro7 = libro.Libro("The Shining", "Sthepen King", "terror")
libro8 = libro.Libro("Cien años de soledad", "Gabriel Garcia Marquez", "ficcion")
libro9 = libro.Libro("1984", "George Orwell", "ficcion")
libro10 = libro.Libro("Don Quijote de la Mancha", "Miguel Cervantes", "ficcion")

libro1.set_isbn()
libro2.set_isbn()
libro3.set_isbn()
libro4.set_isbn()
libro5.set_isbn()
libro6.set_isbn()
libro7.set_isbn()
libro8.set_isbn()
libro9.set_isbn()
libro10.set_isbn()

biblio1.set_inventario(libro1)
biblio1.set_inventario(libro2)
biblio1.set_inventario(libro3)
biblio1.set_inventario(libro4)
biblio1.set_inventario(libro5)
biblio1.set_inventario(libro6)
biblio1.set_inventario(libro7)
biblio1.set_inventario(libro8)
biblio1.set_inventario(libro9)
biblio1.set_inventario(libro10)

santiago = miembro.MiembroBiblioteca("25345889", "Santiago", "santi@gmail.com", "456ss5w")
maria = miembro.MiembroBiblioteca("16456223", "Maria", "mari_a@gmail.com", "jazzs110")
diego = miembro.MiembroBiblioteca("23778110", "Diego", "dieguito_99@gmail.com", "diego777")

biblio1.set_miembro(santiago)
biblio1.set_miembro(maria)
biblio1.set_miembro(diego)

print(biblio1.get_cant_inventario())
print(biblio1.get_cant_miembros())

biblio1.set_prestamos(libro1, santiago)
biblio1.set_prestamos(libro5, maria)
biblio1.set_prestamos(libro6, diego)

print(libro1.estado)
print(libro3.estado)
print(libro10.estado)
print(libro1.isbn)
print(libro3.isbn)
print(libro10.isbn)
print(libro2.estado)

print(biblio1.get_cant_inventario())

biblio1.print_prestamos()
biblio1.print_inventario()


print(biblio1.get_cant_genero("terror"))


        
        





