import requests

url = "https://mashape-community-urban-dictionary.p.rapidapi.com/define"

querystring = {"term":"Hotdog"}

headers = {
	"X-RapidAPI-Key": "c422e4822fmshf03776657fc5ef0p1bd70ajsn82fa76501f89",
	"X-RapidAPI-Host": "mashape-community-urban-dictionary.p.rapidapi.com"
}

response = requests.get(url, headers=headers, params=querystring)

    
# definitions = [item['definition'] for item in response.json()['list']]

# print(definitions)

# print(response.json()['list'])