import pandas

data = pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")
# gray_squirrels = data[data["Primary Fur Color"] == "Gray"]
# print(gray_squirrels)

gray_squirrels_count = len(data[data["Primary Fur Color"] == "Gray"])
red_squirrels_count = len(data[data["Primary Fur Color"] == "Cinnamon"])
black_squirrels_count = len(data[data["Primary Fur Color"] == "Black"])
print(f"total no of gray squirrel are {gray_squirrels_count}")
print(f"total no of red squirrel are {red_squirrels_count}")
print(f"total no of black squirrel are {black_squirrels_count}")

data_dict = {
    "Fur Colour": ["Gray", "Cinnamon", "Black"],
    "Count": [gray_squirrels_count, red_squirrels_count, black_squirrels_count]
}

df = pandas.DataFrame(data_dict)
df.to_csv("Squirrel_count.csv")
