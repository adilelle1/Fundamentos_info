class Player:

    def __init__(self, first_name, last_name, age, country, height, weight, team, games, wins, loses, points, rebounds,
                 assists):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.country = country
        self.height = height
        self.weight = weight
        self.team = team
        self.games = games
        self.wins = wins
        self.loses = loses
        self.points = points
        self.rebounds = rebounds
        self.assists = assists

    def __str__(self) -> str:
        return f"\nNombre: {self.first_name}" \
               f"\nApellido: {self.last_name}" \
               f"\nEdad: {self.age}" \
               f"\nPais: {self.country}" \
               f"\nAltura: {self.height}" \
               f"\nPeso: {self.weight}" \
               f"\nEquipo: {self.team}" \
               f"\nPartidos jugados: {self.games}" \
               f"\nPartidos ganados: {self.wins}" \
               f"\nPartidos perdidos: {self.loses}" \
               f"\nPuntos totales: {self.points}" \
               f"\nRebotes totales: {self.rebounds}" \
               f"\nAsistencias totales: {self.assists}"
