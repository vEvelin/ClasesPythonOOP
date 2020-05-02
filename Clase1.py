# describir una persona
# envejecer
# imprimir

p1_nombre = "Reddy"
p1_edad = 23
p1_genero = "Hombre"


p2_nombre = "Daniel"
p2_edad = 24
p2_genero = "Hombre"

def imprimir_persona(nombre, edad, genero):
    print("nombre: {}, edad: {}, genero: {}".format(nombre, edad, genero))

def aumentar_edad(nombre, edad):
    print("{} tenia: {} y ahora tiene: {}".format(nombre, edad, edad+1))

def aumentar_edad(nombre, edad):
    print("{} tenia: {} y ahora tiene: {}".format(nombre, edad, edad+1))

aumentar_edad(p1_nombre, p1_edad)

'''
Palabras Que debemos recordar siempre
Paradigma Orientado a Objetos

Clase
Objeto
Instanciar o crear
Abstraer
Constructor
'''

'''Resolviendo El Problema con el Paradigma Orientado a Objetos'''

class Persona:

    def __init__(self, edad, ci, nombre, apellido):
        self.edad = edad
        self.ci = ci
        self.nombre = nombre
        self.apellido = apellido

    def imprimir(self):
        print("edad: {}, ci: {}, nombre: {}, apellido: {}".format(self.edad, self.ci, self.nombre, self.apellido))

    def __str__(self):
        return "edad: {}, ci: {}, nombre: {}, apellido: {}".format(self.edad, self.ci, self.nombre, self.apellido)

persona1 = Persona(23, 83123, "reddy", "tintaya")
persona1.imprimir()

persona2 = Persona(30, 12345, "abel", "conde")
persona2.imprimir()

"""
Se escribio la funcion    __str__     haciendo una sobrecarga de operadores
lo que nos permite darle a un objeto una representacion de tipo string para poder imprimila
y asi no usar el metodo imprimir() que suele ser liosa
"""

print(persona1)

print(persona2)


