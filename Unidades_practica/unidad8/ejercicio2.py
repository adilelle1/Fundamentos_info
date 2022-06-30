import random
import requests


class Novela:
    def __init__(self, novela, origen):
        self.__id = random.randint(1, 101)
        self.novela = novela
        self.origen = origen

    def __str__(self) -> str:
        return super().__str__()

    def print_info(self):
        return (f"Novela: {self.novela}"
                f"\nOrigen: {self.origen}")


novelas = []

response = requests.get("https://mocki.io/v1/d4867d8b-b5d5-4a48-a4ab-79131b5809b8")

json = response.json()
for novel in json:
    for k, v in novel.items():
        if k == 'name':
            novela = v
        if k == 'city':
            origen = v
    novela = Novela(novela, origen)
    novelas.append(novela)

for novela in novelas:
    print(novela.__dict__)
    print(novela.print_info())

