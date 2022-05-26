# Ejercicio 5

account1 = {"user_id": "juan", "password": "soyjuan123",
            "saving_bank": {"account_num": "CA-555-113", "amount": 200},
            "current_account": {"account_num": "CC-555-113", "amount": 200},
            "last_trxs": []
            }

account2 = {"user_id": "soledad", "password": "soysole123",
            "saving_bank": {"account_num": "CA-555-112", "amount": 100},
            "current_account": {"account_num": "CC-555-112", "amount": 100},
            "last_trxs": []
            }

account3 = {"user_id": "chiara", "password": "soychiara123",
            "saving_bank": {"account_num": "CA-555-111", "amount": 50},
            "current_account": {"account_num": "CC-555-111", "amount": 50},
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
    # ACCESO DEL USUARIO Y CONTRASEÑA
    print("Ingrese su usuario y contraseña")
    usuario = input("\tusuario: ")
    contrasena = input("\tcontraseña: ")
    indice = 0
    print("\nProcesando...\n")

    for account in accounts:
        # (si coinciden guardo en posición el index y variable acceso pasa a True)
        if account["user_id"] == usuario and account["password"] == contrasena:
            indice = accounts.index(account)
            acceso = True
            break
        # (si no coinciden paso la variable acceso a false y paso a la siguiente iteración)
        else:
            acceso = False
            continue

    # Si el boolean acceso es True, permite acceso, si es False no
    if acceso:
        print(f'Bienvenido/a, {usuario}!')
    else:
        print("------")
        print('ERROR:Permiso denegado - Usuario invalido')
        print("------\n")
        continue


    # Llamo a la función opciones que imprime el menu de acciones
    while True:
        opciones()
        try:
            menu = int(input(">>"))
        except ValueError:
            print("ERROR: No ingresó un número válido")
            print("Por favor, ingrese un número")
            continue

        if menu == 1:  # NO MUESTRA EL PRINT EN CONSOLA
            # Acreditar en CA
            while True:
                try:
                    print("Ingresar cantidad a depositar en caja de ahorro")
                    monto = float(input(">>"))
                    print(f'\nSaldo original caja de ahorro: {accounts[indice]["saving_bank"]["amount"]}')
                    print(f'Ingresaste: {monto}')
                    print('----')

                    for account in accounts:
                        if accounts.index(account) == indice:
                            account["saving_bank"]["amount"] += monto
                            account["last_trxs"].append(f'acreditar en CA: {monto}')
                    print(f'Saldo actualizado caja de ahorro: {accounts[indice]["saving_bank"]["amount"]}')
                    print('----\n')
                    break

                except ValueError:
                    print("ERROR: No ingresó un número")
                    continue

        elif menu == 2:
            # Acreditar en CC
            while True:
                try:
                    print("Ingresar cantidad a depositar en cuenta corriente")
                    monto = float(input(">>"))
                    print(f'\nSaldo original cuenta corriente: {accounts[indice]["current_account"]["amount"]}')
                    print(f'Ingresaste: {monto}')
                    print('----')

                    for account in accounts:
                        if accounts.index(account) == indice:
                            account["current_account"]["amount"] += monto
                            account["last_trxs"].append(f'acreditar en CC: {monto}')
                    print(f'Saldo actualizado cuenta corriente: {accounts[indice]["current_account"]["amount"]}')
                    print('----\n')
                    break

                except ValueError:
                    print("ERROR: No ingresó un número")
                    continue

        elif menu == 3:
            # Consultar saldo en CA
            print(f'Número de cuenta: {accounts[indice]["saving_bank"]["account_num"]}')
            print(f'Saldo caja de ahorro: {accounts[indice]["saving_bank"]["amount"]}')
            print('----\n')

        elif menu == 4:
            # Consultar saldo en CC
            print(f'Número de cuenta: {accounts[indice]["current_account"]["account_num"]}')
            print(f'Saldo cuenta corriente: {accounts[indice]["current_account"]["amount"]}')
            print('----\n')

        elif menu == 5:
            # Consultar Trx
            print('Historial de transacciones: ')
            print('\n\t'.join(map(str, accounts[indice]["last_trxs"])))
            print('----\n')

        elif menu == 6:
            print("\n------Sesión finalizada con éxito------\n")
            break

        else:
            print("Por favor ingrese un número del menú de opciones")
            continue
    continue


