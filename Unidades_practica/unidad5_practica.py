'''#Warming up
sportsmen = []

def insertar_deportista(sportsman,sport):
    deportista = {}
    deportista["sportsman"] = sportsman
    deportista["sport"] = sport
    sportsmen.append(deportista)
    return

def ver_deportista(list):
    for element in list:
        print(f'El/La deportista {element["sportsman"]}, juega {element["sport"]}')
    return


while True:
    print("(1) Insertar un nuevo deportista a la lista")
    print("(2) Ver la lista")

    try:
        option = input(">>")
    except ValueError:
        print("No ingresó un número, vuelva a intentarlo.")
        continue


    if option == "1":
        print("Inserte el nombre del deportista")
        sportsman = input(">>")
        print("Inserte el deporte que practica")
        sport = input(">>")

        insertar_deportista(sportsman,sport)

    elif option == "2":
        ver_deportista(sportsmen)

    else:
        print("No ingrsó un número de la lista, vuelva a intentarlo.")
        continue

#Ejercicio1
shopping_cart = []

def agregar_producto(nombre,cantidad):
    producto = {}
    producto["nombre"] = nombre
    producto["cantidad"] = cantidad
    shopping_cart.append(producto)

def comprar_producto():
    for item in shopping_cart:
        print(f"\tProducto: {item['nombre']}")
        print(f"\tCantidad: {item['cantidad']}")
        print("-----")

while True:
    print("Qué producto desea ingresar al carrito?")
    nombre = input(">>")
    print("Cuantas unidades desea ingresar al carrito?")
    cantidad = int(input(">>"))
    agregar_producto(nombre,cantidad)

    while True:
        print("(1)Ver carrito y comprar")
        print("(2)Continuar viendo productos")
        comprar = input(">>")

        if comprar == "1":
            comprar_producto()
            break

        elif comprar == "2":
            break
    continue

# Ejercicio2 V1

moto = 10
auto = 20
camioneta = 25
camion = 60
camion_acoplado = 90


def imprimir_ticket(vehiculo):
    if vehiculo == "1":
        print(f'Vehículo MOTO, tarifa: ${moto}')
    elif vehiculo == "2":
        print(f'Vehículo AUTO, tarifa: ${auto}')
    elif vehiculo == "3":
        print(f'Vehículo CAMIONETA, tarifa: ${camioneta}')
    elif vehiculo == "4":
        print(f'Vehículo MOTO, tarifa: ${camion}')
    elif vehiculo == "5":
        print(f'Vehículo CAMION ACOPLADO, tarifa: ${camion_acoplado}')



while True:
    print("(1)Moto")
    print("(2)Auto")
    print("(3)Camioneta")
    print("(4)Camión")
    print("(5)Camión acoplado")

    print("Elija una opción del menu")
    vehiculo = input(">>>")

    imprimir_ticket(vehiculo)
    print("---------")

# Ejercicio2 V1
vehiculos = {
    "moto": 10,
    "auto": 20,
    "camioneta": 25,
    "camion": 60,
    "camion acoplado": 90
}

def imprimir_ticket(nombre):
    try:
        tarifa = vehiculos[nombre]
        print("Imprimiendo...")
        print(f"Vehiculo {nombre.upper()} tarifa: ${tarifa}")
        print("---------")
    except KeyError:
        print(f"No se puede encontrar la categoría {nombre}")


def menu_usuario():
    while True:
        print("(1)Moto")
        print("(2)Auto")
        print("(3)Camioneta")
        print("(4)Camión")
        print("(5)Camión acoplado")

        print("Elija una opción del menu")
        vehiculo = input(">>>")

        if vehiculo == "1":
            imprimir_ticket("moto")

        elif vehiculo == "2":
            imprimir_ticket("auto")

        elif vehiculo == "3":
            imprimir_ticket("camioneta")

        elif vehiculo == "4":
            imprimir_ticket("camion")

        elif vehiculo == "5":
            imprimir_ticket("camion acoplado")

        else:
            print("Opción invalida")



menu_usuario()

# Ejercicio3
alumnos = [{'001': [7, 4, 6]}, {"002": [4, 9, 9]}, {"003": [10, 7, 8]}]

nota_final = []

def calculo_nota_final(lista):
    for alumno in lista:
        for k,v in alumno.items():
            nota = {}
            nota[k] = round((sum(v)/len(v)))
            nota_final.append(nota)


calculo_nota_final(alumnos)

def ver_nota_final(nota_final):
    for dic in nota_final:
        for k,v in dic.items():
            print(f"El alumno con ID {k} obtuvo una calificación final de {v}")

ver_nota_final(nota_final)

# Ejercicio4

recetas_favoritas = [{"pollo al curry":["pollo","curry","papa"]},
                     {"ensalada":["lechuga","tomate","zanahoria","cebolla"]},
                     {"tarta de morron":["masa de tarta","queso","cebolla","morron", "tomate"]},
                     {"milanesas de pollo":["pollo","pan rallado","papa"]},
                     {"salmon marinado":["arroz","salmon","soja"]}]


def recipe_recommender():
    print("Ingrese dos ingredientes")
    ingrediente1 = input("Ingrediente 1 >>")
    ingrediente2 = input("Ingrediente 2 >>")
    for receta in recetas_favoritas:
        for k,v in receta.items():
            if ingrediente1 in v and ingrediente2 in v:
                print(f"Podrías preparar {k}")


recipe_recommender()

# Ejercicio4 bis
recetas_favoritas = [{"receta": "pollo al curry", "ingredientes": ["pollo", "curry", "papa"]},
                     {"receta": "ensalada", "ingredientes": ["lechuga", "tomate", "zanahoria", "cebolla"]},
                     {"receta": "tarta de morron",
                      "ingredientes": ["masa de tarta", "queso", "cebolla", "morron", "tomate"]},
                     {"receta": "milanesas de pollo", "ingredientes": ["pollo", "pan rallado", "papa"]},
                     {"receta": "salmon marinado", "ingredientes": ["arroz", "salmon", "soja"]}]

ingredients = []


def recommender(lista):
    recetas_recomendadas = []

    for input in ingredients:
        for receta in recetas_favoritas:
            for ingredientes in receta["ingredientes"]:
                if input in ingredientes:
                    if not (receta["receta"] in recetas_recomendadas):
                        recetas_recomendadas.append(receta["receta"])
    return recetas_recomendadas

def print_recipes(recetas_reco):
    for recipe in recetas_reco:
        print(f"\nReceta: {recipe['receta']}")
        for ingredient in recipe['ingredientes']:
            print(f"\t* {ingredient}")


def menu():
    while True:
        print("(1) - Agregar ingrediente")
        print("(2) - Buscar receta")
        print("(3) - Salir")

        option = input(">>")

        if option == "1":
            ingrediente = input("Ingrediente>>")
            ingredients.append(ingrediente)
        elif option == "2":
            if len(ingredients) >= 2:
                recipe = recommender(ingredients)
                print_recipes(recipe)
            else:
                print("Debes ingresar al menos dos ingredientes")

        elif option == "3":
            break
        else:
            print("Ingresaste un numero invalido, vuelve a intentarlo")
            continue


menu()

# Ejercicio5
db_movies = [{"movie": "Star Wars: Episodio VII", "availability": 6},
             {"movie": "The Lord of the rings", "availability": 2},
             {"movie": "Back to the future", "availability": 3},
             {"movie": "Pulp fiction", "availability": 2},
             {"movie": "Avatar", "availability": 1},
             {"movie": "Batman: Dark Knight", "availability": 0},
             {"movie": "Jumanji", "availability": 5},
             {"movie": "El secreto de sus ojos", "availability": 8}]

def main_menu():
    print("\nPlease select your next action")
    print("\t(1)Rent another movie")
    print("\t(2)Quit")
    option = input("\t>>")

    if option == "1":
        process()


def rent_movie(client_id, movie):
    print(f'The movie {movie.upper()} was rented by the client ID: {client_id}')


def renting_menu(choice):
    print("\nTo continue, please login using your client ID")
    client_id = input(">>")

    print("\nPlease select your next action")
    print("\t(1)Rent movie")
    print("\t(2)Search for another movie")
    print("\t(3)Quit")
    option = input("\t>>")

    if option == "1":
        rent_movie(client_id, choice)


def search_movie(movies, choice):
    for movie in movies:
        for k,v in movie.items():

            if choice == movie["movie"]:
                if movie["availability"] > 0:
                    print(f'The movie {choice.upper()} is available')
                    renting_menu(choice)
                    return
                elif movie["availability"] == 0:
                    print(f'The movie {choice.upper()} is NOT available')
                    print("Please try again with another movie\n")
                    return
                break

            elif choice != movie["movie"]:
                if movie != db_movies[-1]:
                    continue
                elif movie == db_movies[-1]:
                    print(f'The movie {choice.upper()} does not exist in this store')
                    print("Please try again with another movie\n")
                    return
            break

rented_movies = []

def process():
    while True:
        print("Please insert the title you are looking for")
        choice = input(">>")
        search_movie(db_movies, choice)
        break
    main_menu()


process()
'''

# Ejercicio 6
manufacturing_cars = [{'model': 'Mondeo', 'engine': '2.0'},
                      {'model': 'Focus', 'engine': '1.6'},
                      {'model': 'Mondeo', 'engine': '2.0'},
                      {'model': 'Mondeo', 'engine': '2.0'},
                      {'model': 'Raptor', 'engine': '3.5'},
                      {'model': 'Focus', 'engine': '1.6'},
                      {'model': 'Focus', 'engine': '1.6'},
                      {'model': 'Raptor', 'engine': '3.5'},
                      {'model': 'Focus', 'engine': '1.6'},
                      {'model': 'Raptor', 'engine': '3.5'},
                      {'model': 'Mondeo', 'engine': '2.0'},
                      {'model': 'Mondeo', 'engine': '2.0'}
                      ]

car_colours = ['white', 'dark gray', 'red', 'black']

import random


def paint_car(car, ):
    colour = random.choice(car_colours)
    car["colour"] = colour
    return


while True:
    for cars in manufacturing_cars:
        for car in cars:
            paint_car(car)
            print(car)
