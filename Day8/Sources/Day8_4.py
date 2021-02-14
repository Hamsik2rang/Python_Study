import pandas as pd

data = pd.read_csv("./Day8/Resources/2018_Central_Park_Squirrel_Data.csv")

grey_squirral_count = len(data[data["Primary Fur Color"] == "Gray"])
red_squirral_count = len(data[data["Primary Fur Color"] == "Red"])
black_squirral_count = len(data[data["Primary Fur Color"] == "Black"])


data_dict = {
    "Color": ["Grey", "Red", "Black"],
    "Count": [grey_squirral_count, red_squirral_count, black_squirral_count],
}

df = pd.DataFrame(data_dict)

df.to_csv("./Day8/Resources/squirral_count.csv")