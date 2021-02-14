import pandas

data = pandas.read_csv("./Day8/Resources/weather_data.csv")
list_data = data["temp"].to_list()


monday_temp = data[data.day == "Monday"].temp

monday_temp_fh = (monday_temp * 9 / 5) + 32
print(monday_temp_fh)
