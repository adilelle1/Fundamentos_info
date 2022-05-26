class Team:

    def __init__(self, name, alias, city, state, championships, conference, games, wins, loses):
        self.name = name
        self.alias = alias
        self.city = city
        self.state = state
        self.championships = championships
        self.conference = conference
        self.games = games
        self.wins = wins
        self.loses = loses

    def __str__(self) -> str:
        return f"\nNombre: {self.name}" \
               f"\nAlias: {self.alias}" \
               f"\nCiudad: {self.city}" \
               f"\nEstado: {self.state}" \
               f"\nCampeonatos: {self.championships}" \
               f"\nConferencia: {self.conference}" \
               f"\nPartidos jugados: {self.games}" \
               f"\nPartidos ganados: {self.wins}" \
               f"\nPartidos perdidos: {self.loses}"

