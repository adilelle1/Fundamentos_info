from restaurantes import Restaurante

restaurants = []

kansas_menu = ['BBQ Ribs', 'Rib eye steak', 'Arizona Pasta']
tana_menu = ['Mushrooms pizza', 'Mozzarella pizza', 'Melanzane pizza']
lima_menu = ['Phila roll', 'Nigiri', 'Sashimi']

kansas = Restaurante('Kansas Grill & Bar', 'American', '11-24', kansas_menu)
tana = Restaurante('Tana', 'Pizza', '18 - 1', tana_menu)
lima = Restaurante('Lima', 'Sushi', '12 - 23', lima_menu)

restaurants.append(kansas)
restaurants.append(tana)
restaurants.append(lima)

while True:
    print('Welcome to your gastronomic tour!')
    count = 0
    for restaurant in restaurants:
        print(f'\t{restaurant.nombre}')
    print('Please insert the name of the restaurant you would like to see ')
    option = input('>>>')

    for restaurant in restaurants:
        if option == restaurant.nombre:
            restaurant.describe_restaurant()
            if restaurant.is_open:
                print("The restaurant is OPEN")
            else:
                print("The restaurant is CLOSED")
            print("What's next?")
            print("\t 1. See the menu")
            print("\t 2. See other restaurant")
            opt = input('>>>')
            if opt == '1':
                restaurant.get_menu()
            elif opt == '2':
                break


    break
