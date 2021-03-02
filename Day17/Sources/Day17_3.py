import requests
from datetime import datetime

parameters = {"lat": 36.94010, "lng": 126.42809, "date": "today", "formatted": 0}


def raw_time_to_dict(raw):
    element = raw.split("T")
    date = element[0].split("-")
    time = element[1].split(":")
    time[2] = time[2][:2]
    result = {"date": date, "time": time}
    return result


response = requests.get(url="https://api.sunrise-sunset.org/json", params=parameters)
response.raise_for_status()
# get data of UTC
data = response.json()
sunrise = data["results"]["sunrise"]
sunset = data["results"]["sunset"]

sunrise_dict = raw_time_to_dict(sunrise)
sunset_dixt = raw_time_to_dict(sunset)

sunrise_date = list(map(int, sunrise_dict["date"]))
sunrise_time = list(map(int, sunrise_dict["time"]))
sunset_date = list(map(int, sunrise_dict["date"]))
sunset_time = list(map(int, sunrise_dict["time"]))

utc_sunrise = datetime(
    year=sunrise_date[0],
    month=sunrise_date[1],
    day=sunrise_date[2],
    hour=sunrise_time[0],
    minute=sunrise_time[1],
    second=sunrise_time[2],
)
# TODO: Convert UTC to KST. How can i do it?
# print(utc_sunrise)

# utc_sunrise_timestamp = utc_sunrise.strptime(utc_sunrise, "%Y-%M-%d %H:%M:%S")
# print(utc_sunrise_timestamp)
# local_sunrise = datetime.fromtimestamp(utc_sunrise_timestamp)
# print(local_sunrise)
