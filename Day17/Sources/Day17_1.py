import requests

responce = requests.get(url="http://api.open-notify.org/iss-now.json")
responce.raise_for_status()

data = responce.json()

longitude = data["iss_position"]["longitude"]
latitude = data["iss_position"]["latitude"]
iss_position = (longitude, latitude)

print(iss_position)