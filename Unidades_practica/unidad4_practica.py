'''
#Ejercicio 1
print("\n------------")
print("WELCOME TO DISNEY WORLD")
print("------------\n")
print("Please, to buy a ticket enter your age: ")

while True:
    age = input(">>")
    if age == "quit":
        break
    age = int(age)
    try:
        if age < 5:
            print("Your ticket costs 0, congratulations you have a free ticket!")
        elif age >= 5 and age < 9:
            print("Your ticket costs only U$15!")
        elif age >= 9 and age < 14:
            print("Your ticket costs only U$23!")
        elif age >= 14 and age < 100:
            print("Your ticket costs only U$35!")
        else:
            print("You'r awesome!! Free ticket for you!")
    except ValueError:
        print("You must enter a number bigger than 0")

# Ejercicio 3 TERMINARLO

orders = []
print(orders)
while True:
    print("Ingresar nombre del medicamento")
    med = input(">>")

    print("Ingresar nombre del laboratorio")
    lab = input(">>")

    print("Ingresar cantidad")
    quant = input(">>")

    items = {}

    if med not in orders and lab not in orders and quant not in orders:
        items["medicamento"] = med
        items["laboratorio"] = lab
        items["cantidad"] = quant
        orders.append(items)
        print(orders)
    else:
        print("El medicamento ya existe en el inventario")
        break

#Ejercicio 4
lavados = []

while True:
    print("--------")
    print("Bienvenidos")
    print("--------")

    print("Menu")
    print("\t(1)Lavanderia")
    print("\t(2)Recepción")
    print("\n--------")
    menu = input(">>")
    if menu == "1":
        clientes = {}

        print("Ingresar número de habitación")
        habitacion = input(">>")

        print("Ingresar cantidad de prendas")
        prendas= input(">>")

        print("Ingresar fecha")
        fecha = input(">>")

        clientes["número habitación"] = habitacion
        clientes["cantidad prendas"] = prendas
        clientes["fecha"] = fecha
        lavados.append(clientes)
    elif menu == "2":
        print(lavados)
'''
# Ejercicio 5

account1 = {"user_id": "juan", "password": "soyjuan123",
            "saving_bank": {"account_num": "CA-555-113", "amount": 0},
            "current_account": {"account_num": "CC-555-113", "amount": 100},
            "last_trxs": []
             }

account2 = {"user_id": "soledad", "password": "soysole123",
            "saving_bank": {"account_num": "CA-555-112", "amount": 100},
            "current_account": {"account_num": "CC-555-112", "amount": 1},
            "last_trxs": []
            }

account3 = {"user_id": "chiara", "password": "soychiara123",
            "saving_bank": {"account_num": "CA-555-111", "amount": 1},
            "current_account": {"account_num": "CC-555-111", "amount": 1},
            "last_trxs": []
            }

accounts = [account1, account2, account3]


def bienvenida():
    print('\t{:17}'.format('---------') + '---------')
    print('\t{:23}'.format('---') + '---')
    print('\t---' + '{:^20}'.format('Banco Digital LA') + '---')
    print('\t{:23}'.format('---') + '---')
    print('\t{:17}'.format('---------') + '---------')

def opciones():
    print("Menu")
    print("\t(1)Acreditar en CA")
    print("\t(2)Acreditar en CC")
    print("\t(3)Consultar saldo en CA")
    print("\t(4)Consultar saldo en CC")
    print("\t(5)Consultar Trx")
    print("\t(6)Salir")
    print("Elija la acción que desea realizar:")

acceso = True

bienvenida()
while True:
    #ACCESO DEL USUARIO Y CONTRASEÑA
    print("Ingrese su usuario y contraseña")
    usuario = input("\tusuario: ")
    contrasena = input("\tcontraseña: ")
    indice = 0
    print("\nProcesando...\n")
    for account in accounts:
        #(si coinciden guardo en posición el index y variable acceso pasa a True)
        if account["user_id"] == usuario and account["password"] == contrasena:
            indice = accounts.index(account)
            acceso = True
            break
        #(si no coinciden paso la variable acceso a false y paso a la siguiente iteración)
        else:
            acceso = False
            continue
    # Si el boolean acceso es True, permite acceso, si es False no
    if acceso == True:
        print(f'Bienvenido, {usuario}!')
    else:
        print('Permiso denegado - Usuario invalido')
        continue
    print("\n")
    #Llamo a la función opciones que imprime el menu de acciones
    while True:
        opciones()
        menu = input(">>")
        print("\n")
        if menu == 1: # NO MUESTRA EL PRINT EN CONSOLA
            # Acreditar en CA
            print("Ingresar cantidad a depositar en caja de ahorro")
            monto = int(input(">>"))
            print(f'Saldo original caja de ahorro: {accounts[indice]["saving_bank"]["amount"]}')
            print(f'Ingresaste: {monto}')
            print('----')
            for account in accounts:
                if accounts.index(account) == indice:
                    account["saving_bank"]["amount"] += monto
            print(f'Saldo actualizado caja de ahorro: {accounts[indice]["saving_bank"]["amount"]}')

        elif menu == 2:
            # Acreditar en CC
            print("Ingresar cantidad a depositar en cuenta corriente")
            monto = int(input(">>"))
            print(f'Saldo original cuenta corriente: {accounts[indice]["current_account"]["amount"]}')
            print(f'Ingresaste: {monto}')
            print('----')
            for account in accounts:
                if accounts.index(account) == indice:
                    account["current_account"]["amount"] += monto
            print(f'Saldo actualizado cuenta corriente: {accounts[indice]["current_account"]["amount"]}')

        elif menu == 3:
            # Consultar saldo en CA
            print(f'Número de cuenta: {accounts[indice]["saving_bank"]["account_num"]}')
            print(f'Saldo caja de ahorro: {accounts[indice]["saving_bank"]["amount"]}')

        elif menu == 4:
            # Consultar saldo en CC
            print(f'Número de cuenta: {accounts[indice]["current_account"]["account_num"]}')
            print(f'Saldo cuenta corriente: {accounts[indice]["current_account"]["amount"]}')

        elif menu == 5:
            # Consultar Trx
            print(f'Historial de transacciones: {accounts[indice]["last_trxs"]}')

        else:
            break
    break
