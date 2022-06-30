class Restaurante:

    def __init__(self, nombre, tipo, open_daily, menu):

        self.nombre = nombre
        self.tipo = tipo
        self.is_open = False
        self.open_daily = open_daily
        self.menu = menu

    def describe_restaurant(self):
        print(f'Restaurant name: {self.nombre}')
        print(f'Type: {self.tipo}')

    def open_restaurant(self):
        self.is_open = True
        print(f'The restaurant {self.nombre} is open!')

    def closed_restaurant(self):
        self.is_open = False
        print(f'We are sorry, the restaurant {self.nombre} is closed.')

    def get_menu(self):
        print(f"{self.nombre}'s menu:")
        for i in self.menu:
            print(f'\t{i}')

    def __str__(self) -> str:
        return super().__str__()




