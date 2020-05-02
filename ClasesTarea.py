print("----------------CLASE REFUGIO ANIMAL-------------------")
class Refugio_Aanimal():
    def __init__(self, nombreEspecie, color, tamaño, genero):
        self.nombreEspecie = nombreEspecie
        self.color = color
        self.tamaño = tamaño
        self.genero = genero

    def __str__(self):
     return "nombreEspecie: {}, color: {}, tamaño: {}, genero: {}".format(self.nombreEspecie, self.color, self.tamaño,self.genero)

    def alimentar(self):
        print("La especie : " +self.nombreEspecie +" fue alimentado")
    def trasladar(self):
        print("La especie : "+ self.nombreEspecie +" Fue trasladado")
    def liberar(self):
        print("La especie : " +self.nombreEspecie +"  Fue liberado")
    def rescatar(self):
        print("Las especie : " + self.nombreEspecie +" Fue rescatada")


zoo1 = Refugio_Aanimal("oso","cafe","mediano","macho")
print(zoo1)
zoo1.alimentar()
zoo1.trasladar()
zoo2 = Refugio_Aanimal ("Tucan", "negro", "pequeño","macho")
print(zoo2)
zoo2.alimentar()
zoo2.liberar()
zoo3 = Refugio_Aanimal("mono_capuccino","cafe","mediano","hembra")
print(zoo3)
zoo1.rescatar()
zoo2.rescatar()
zoo3.rescatar()


print("------------------CLASE ELECTRODOMESTICO-------------")
class Electrodomestico():
    def __init__(self,nombre,precio,caracteristicas,cantidad):
        self.nombre = nombre
        self.precio = precio
        self.caracteristicas= caracteristicas
        self.cantidad = cantidad
    def __str__(self):
        return "nombre {}, precio {}, caracteristicas {},cantidad {}".format(self.nombre,self.precio,self.caracteristicas, self.cantidad)
    def vender(self):
        print("El producto"+ self.nombre +"ha sido vendido")
        print("Actualizando cantidad del producto  : " + self.nombre +" ")
        self.cantidad =self.cantidad- 1
        print(self.cantidad)
    def nuevo_pedido(self):
        print("Realizar nuevo Pedido del producto : "+ self.nombre)
    def emite_factura(self):
        print("Datos para la factura del producto : " + self.nombre + "  precio : " + str(self.precio))

elec1 = Electrodomestico("licuadora",120,"xyz",20)
print(elec1)
elec2 = Electrodomestico("Microondas",360,"abcd",10)
print(elec2)
elec3 = Electrodomestico ("Lavadora",8000,"abcdef",12)
print(elec3)
elec1.vender()
elec1.nuevo_pedido()
elec1.emite_factura()
elec2.nuevo_pedido()
elec2.vender()
elec3.vender()