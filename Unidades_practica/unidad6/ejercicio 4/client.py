import random


class Client:

    def __init__(self, name, last_name, phone_number, document, address, category, debit_card, credit_card=None):
        self.id = random.randrange(10000000)
        self.name = name
        self.last_name = last_name
        self.phone_number = phone_number
        self.document = document
        self.address = address
        self.category = category
        self.is_client_active = True
        self.debit_card = debit_card
        self.credit_card = credit_card

    def add_credit_card(self, credit_card):
        self.credit_card = credit_card

    def add_debit_card(self, debit_card):
        self.debit_card = debit_card

    def upgrade_category(self, new_category):
        self.category = new_category
        if self.debit_card:
            self.debit_card.up_category(new_category)
        if self.credit_card:
            self.credit_card.up_category(new_category)


    def __str__(self):
        print(f"\n Nombre completo: {self.name}, {self.last_name}")
        print(f"Numero de telefono: {self.phone_number}")
        print(f"Documento de identidad: {self.document}")
        print(f"Direccion: {self.address}")
        print(f"Categoria: {self.category}")
        print(f"\n----------- Tajertas -----------")
        print(f"Tarjeta de DEBITO: {self.debit_card}")

        if self.credit_card:
            print(f"\nTarjeta de CREDITO: {self.credit_card}")
