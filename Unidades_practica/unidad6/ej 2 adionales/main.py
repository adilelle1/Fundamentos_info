from vehiculos import Auto, Moto, Bicicleta, Velero


def menu():
    print("Menu vehiculos")
    print("Elija la opcion con el vehiculo que desea probar")
    print("\t(1). Auto")
    print("\t(2). Moto")
    print("\t(3). Velero")
    print("\t(4). Bicicleta")
    return int(input(">>"))


auto = Auto("auto", "2015", "BMW series x", "trx234", 3, 4, 3)
moto = Moto("auto", "2015", "Royal enfield - assure", "wert123", 2, 4)
velero = Velero("auto", "2015", 18, 10, "wert123", 10)
bici = Bicicleta("bicicleta", "2011", "Mountain Bike", 6, 2)

print(auto.print_info())
print(auto.move_forward())
print(auto.fix_flat_tire())
print(auto.move_forward())
print(auto.move_forward())
print(auto.refueling())
print(auto.move_forward())

'''
while True:
    print("Bienvenido")
    option = menu()
    if option == 1:
        auto'''
