'''
#Definir clase

class Ballena:

    def __init__(self, nombre, edad, sexo, peso, mamifero):
        self.nombre = nombre
        self.edad = edad
        self.sexo = sexo
        self.peso = peso
        self.mamifero = mamifero

    def nadar(self):
        return f"{self.nombre} esta nadando..."

    def saltar(self):
        return f"{self.nombre} esta saltando..."

    def comer(self):
        return f"{self.nombre} esta comiendo..."

    def descansar(self):
        return f"{self.nombre} esta Zzz..."

    def estado(self):
        return f"Estado de la Ballena:" \
               f"\n\tNombre:{self.nombre}" \
               f"\n\tEdad: {self.edad}" \
               f"\n\tSexo: {self.sexo}" \
               f"\n\tPeso:{self.peso}" \
               f"\n\tMamifero: {'SI'if self.mamifero else 'NO'}"

alejo = Ballena('Alejo',23,'M',90,True)
print(alejo.nadar())
print(alejo.saltar())
print(alejo.comer())
print(alejo.descansar())
print(alejo.estado())

#Ejercicio 1
from shapes import Cubo, Esfera, PrismaRectangular

print("Menu de opciones")
print("Qué figura geométrica deseas imprimir?")
print("(1)Esfera")
print("(2)Cubo")
print("(3)Prisma Rectangular")
option = input(">>")


if option == "1":
    print("Ingrese las dimensiones de su esfera:")
    radio = input("Radio en cm:")
    esfera = Esfera(radio)
    print(f'\nImprimiento...{esfera.nombre} por favor espere')
    print(f'\n{esfera.print_properties()}')

elif option == "2":
    print("Ingrese las dimensiones de su cubo:")
    lado = input("Lado en cm:")
    cubo = Cubo(lado)
    print(f'\nImprimiento...{cubo.nombre} por favor espere')
    print(f'\n{cubo.print_properties()}')

elif option == "3":
    print("Ingrese las dimensiones de su prisma:")
    base = input("Base en cm:")
    altura = input("Altura en cm:")
    profundidad = input("Profundidad en cm:")
    prisma = PrismaRectangular(base, altura, profundidad)
    print(f'\nImprimiento...{prisma.nombre} por favor espere')
    print(f'\n{prisma.print_properties()}')


# Ejercicio 3

class Lamparas:

    def __init__(self, fabricante, codigo_fabricante, modelo, amperaje, potencia, diametro, eficiencia_energetica,
                 precio):
        self.__fabricante = fabricante
        self.__codigo_fabricante = codigo_fabricante
        self.modelo = modelo
        self.amperaje = amperaje
        self.potencia = potencia
        self.diametro = diametro
        self.eficiencia_energetica = eficiencia_energetica
        self.precio = precio


npn = Lamparas('Pfizer', '001123', 'deluxe', 220, '4MA', 5, '12w/s', 250)

'''

# Ejercicio 4

