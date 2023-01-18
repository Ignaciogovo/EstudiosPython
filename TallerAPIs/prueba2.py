import requests
import datos as dt
url = "https://api-football-v1.p.rapidapi.com/v3/players"
querystring = {"league":"140","season":"2022"}

response = dt.extraer(url,querystring)

print(response.text)

f=open("EstadisticasJugadores.json","w")
f.write(response.text)
f.close()
