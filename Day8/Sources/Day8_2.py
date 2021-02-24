import csv

TEMPERATURE = 1

with open("./Day8/Resources/weather_data.csv", "r") as f:
    data = csv.reader(f)
    temperatures = []
    for col in data:
        for row in col:
            print(row)