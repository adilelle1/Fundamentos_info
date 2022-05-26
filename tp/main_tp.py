from team import Team
from player import Player

west_conference = "WEST"
east_conference = "EAST"

lakers = Team("Los Angeles Lakers", "LAK", "Los Angeles", "California", 33, west_conference, 82, 50, 32)
bulls = Team("Chicago Bulls", "BUL", "Chicago", "Illinois", 23, east_conference, 82, 72, 10)
warriors = Team("Golden State Warriors", "GSW", "San Francisco", "Chicago", 20, west_conference, 82, 65, 17)

stephen_curry = Player("Stephen", "Curry", 30, "United States", 192, 88, warriors.name, warriors.games, warriors.wins,
                       warriors.loses, 1000, 600, 700)

lebron_james = Player("LeBron", "James", 37, "United States", 207, 105, lakers.name, lakers.games, lakers.wins, lakers.loses,
                      1500, 1000, 1000)

demar_derozan = Player("Demar", "DeRozan", 32, "United States", 200, 95, bulls.name, bulls.games, bulls.wins, bulls.loses,
                      900, 700, 500)



print(lebron_james)

