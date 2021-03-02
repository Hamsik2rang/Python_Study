import requests
from datetime import datetime
import time

parameters = {"lat": 12.34567, "lng": 123.45678, "date": "today", "formatted": 0}


def raw_time_to_dict(raw):
    element = raw.split("T")
    date = element[0].split("-")
    time = element[1].split(":")
    time[2] = time[2][:2]
    result = {"date": date, "time": time}
    return result


def get_datetime(date, time):
    result = datetime(date[0], date[1], date[2], time[0], time[1], time[2])
    return result


def from_UTC_to_local(utc):
    now_local_timestamp = time.time()
    offset = datetime.fromtimestamp(now_local_timestamp) - datetime.utcfromtimestamp(
        now_local_timestamp
    )
    return utc + offset


response = requests.get(url="https://api.sunrise-sunset.org/json", params=parameters)
response.raise_for_status()
# get data of UTC
data = response.json()
sunrise = data["results"]["sunrise"]
sunset = data["results"]["sunset"]

sunrise_dict = raw_time_to_dict(sunrise)
sunset_dict = raw_time_to_dict(sunset)

sunrise_date = list(map(int, sunrise_dict["date"]))
sunrise_time = list(map(int, sunrise_dict["time"]))
sunset_date = list(map(int, sunset_dict["date"]))
sunset_time = list(map(int, sunset_dict["time"]))

utc_sunrise = get_datetime(sunrise_date, sunrise_time)
utc_sunset = get_datetime(sunset_date, sunset_time)

# TODO: Convert UTC to KST. How can i do it?
# ----> It Works!
local_sunrise = from_UTC_to_local(utc_sunrise)
local_sunset = from_UTC_to_local(utc_sunset)

print(f"Today's Sunrise Time : {local_sunrise}")
print(f"Today's Sunset Time : {local_sunset}")