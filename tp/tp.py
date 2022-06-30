
import requests
'''
#conn = http.client.HTTPSConnection("api-nba-v1.p.rapidapi.com")
response = requests.get(
    "https://api-nba-v1.p.rapidapi.com/players/statistics?season=2020&team=6",
    headers = {
    'x-rapidapi-host': "api-nba-v1.p.rapidapi.com",
    'x-rapidapi-key': "1e5e5821femsh450b4f3086376a6p114414jsne8cc7f313f90"
    }
)

print(response.text)
#conn.request("GET", "/players/statistics?season=2020&", headers=headers)

#res = conn.getresponse()
#data = res.read()

#print(data.decode("utf-8"))

import requests
from teams import welcome,user_menu,team_finder

while True:
    welcome()
    user_menu()
    menu_option = input('>>')
    team = str(team_finder())

    response = requests.get(
        "https://api-nba-v1.p.rapidapi.com/players/statistics?season=2020&team=" + team,
        headers={
            'x-rapidapi-host': "api-nba-v1.p.rapidapi.com",
            'x-rapidapi-key': "1e5e5821femsh450b4f3086376a6p114414jsne8cc7f313f90"
        }
    )

    status_code = response.status_code

    print('Insert your player attributes:')
    points = input('Points:')
    assists = input('Assists:')
    rebounds = input('Rebounds:')
    minutes = input('Minutes played:')

    if status_code == 200:
        json = response.json()
        for dict in json['response']:
            for k,v in dict['player'].items():
                print(v)
        # response es una key del json, su value es una lista de diccionarios
    else:
        print('Error')'''
import requests

team = input("\nInsert your team's name>>")

response = requests.get(
    "https://api-nba-v1.p.rapidapi.com/teams?search=" + team,
    headers={
        'x-rapidapi-host': "api-nba-v1.p.rapidapi.com",
        'x-rapidapi-key': "1e5e5821femsh450b4f3086376a6p114414jsne8cc7f313f90"
    }
)

status_code = response.status_code

if status_code == 200:
    json = response.json()
    # print(json['response']) -- permite ver todos los atributos
    print(json)