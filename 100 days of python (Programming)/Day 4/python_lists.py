
states_of_India = ["Andhra Pradesh", "Arunachal Pradesh", "Bihar", "Chhattisgarh", "Goa", "Gujarat",
                   "Haryana", "Himachal Pradesh", "Jharkhand", "Karnataka", "Kerala", "Assam",
                   "Madhya Pradesh", "Maharashtra", "Manipur", "Meghalaya", "Mizoram", "Nagaland",
                   "Odisha", "Punjab", "Rajasthan", "Sikkim", "Tamil Nadu", "Telangana", "Tripura",
                   "Uttarakhand", "Uttar Pradesh", "West Bengal"]

print(states_of_India[2])

states_of_India[0] = "Bihar"
print(states_of_India[0])

states_of_India.append("Jammu and kashmir")         # append function add the item to the end of list
print(states_of_India)

states_of_India.extend(["Rajendra Prasad Land"])      # extend function is used to extend the list
print(states_of_India)
