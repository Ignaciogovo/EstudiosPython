import requests

url = "https://api-football-v1.p.rapidapi.com/v3/teams"

querystring = {"league":"140","season":"2010"}

headers = {
	"X-RapidAPI-Key": "key",
	"X-RapidAPI-Host": "api-football-v1.p.rapidapi.com"
}

response = requests.request("GET", url, headers=headers, params=querystring)

print(response.text)

f=open("La_Liga.json","w")
f.write(response.text)
f.close()
