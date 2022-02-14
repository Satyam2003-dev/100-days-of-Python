# with open("weather_data.csv") as data_file:
#     data = data_file.readlines()
#     print(data)

# import csv
#
# with open("weather_data.csv") as data_file:
#     data = csv.reader(data_file)
#     temperatures = []
#     for row in data:
#         if row[1] != "temp":
#             temperatures.append(int(row[1]))
#
#     print(temperatures)

import pandas

data = pandas.read_csv("weather_data.csv")
# print(data)
# print(data["temp"])
# print(data["day"])
# print(data["condition"])

# print(type(data))
#
# print(type(data["temp"]))

# data_dict = data.to_dict()
# print(data_dict)
#
# temp_list = data["temp"].to_list()
# print(temp_list)
# print(len(temp_list))
#
# # average = sum(temp_list) / len(temp_list)
# # print(average)
#
# print(data["temp"].mean())
# print("\n")
# print(data["temp"].max())
#
# # get data in column
#
# print(data["condition"])
# print("\n")
# print(data.condition)

# get data in row

# print(data[data.day == "Monday"])
#
# print(data[data.temp == data.temp.max()])
#
# monday = data[data.day == "Monday"]
# print(monday.condition)
# monday_temp = int(monday.temp)
# monday_temp_f = monday_temp * 9/5 + 32
# print(monday_temp_f)

# create a dataframe from scratch

data_dict = {
    "students": ["Amy", "Jack", "Peter"],
    "marks": [75, 85, 70]
}
data = pandas.DataFrame(data_dict)
data.to_csv("new_data.csv")
