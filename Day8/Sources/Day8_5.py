import pandas as pd

data = pd.read_csv("./Day8/Resources/postal_codes_and_addresses.csv", encoding="cp949")


input_city_info = input().split()

df_list = []
for city_info in input_city_info:
    df = data[data.city.str.contains(city_info, regex=False)]
    df_list.append(df)


for i in range(1, len(df_list)):
    df_list[0] = pd.merge(df_list[0], df_list[i])

result = df_list[0]
del df_list

result.to_csv("./Day8/Resources/searched_postal_codes.csv")
