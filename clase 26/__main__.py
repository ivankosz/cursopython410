from hotel import Hotel
from habitacion import Habitacion
from huesped import Huesped

#crear hotel
hotel_1 = Hotel("Hotel Nacional", "7 1429", "4836318")

#crear habitaciones

hab1 = Habitacion(200, 1001)
hab2 = Habitacion(250, 1002)
hab3 = Habitacion(250, 1003)
hab4 = Habitacion(350, 1004)
hab5 = Habitacion(350, 1005)

#crear huespedes nombre, apellido, habitacion, noches

host1 = Huesped("Dario", "Selva")
host2 = Huesped("Sergio", "Rego")
host3 = Huesped("Martin", "Daddario")

#set huespedes

hotel_1.set_habitacion(hab1)
hotel_1.set_habitacion(hab2)
hotel_1.set_habitacion(hab3)
hotel_1.set_habitacion(hab4)
hotel_1.set_habitacion(hab5)

hotel_1.set_registro_huesped(host1, hab3, 4)

print (host1.get_habitacion())

print(hab3.get_estado())

