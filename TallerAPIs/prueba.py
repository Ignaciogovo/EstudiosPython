# import requests
import json

# url = "https://api-football-v1.p.rapidapi.com/v3/leagues"

# headers = {
# 	"X-RapidAPI-Key": key,
# 	"X-RapidAPI-Host": "api-football-v1.p.rapidapi.com"
# }

# response = requests.request("GET", url, headers=headers)

# print(response.text)
# f=open("ligas.json","w")
# f.write(response.text)
# f.close()



f=open('ligas.json', 'r')
datos = json.load(f)
print(type(datos))

# Buscar datos de las ligas
# for value in datos["response"]:
#     country=value['country']
#     if country['name'] == 'Spain':
#         league = value['league']
#         seasons = value["seasons"]
#         years=[]
#         for season in seasons:
#             years.append(season["year"])
#         print(league["name"]+" id: "+str(league["id"]))
#         print(years)




# Buscar datos de los clubes
f=open('La_Liga.json', 'r')
datos = json.load(f)
print(type(datos))
for teams in datos["response"]:
    team=teams["team"]
    print(team["name"])

