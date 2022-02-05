
# https://pypi.org/project/prettytable/
from prettytable import PrettyTable
table = PrettyTable()
# row by row
table.field_names = ["Pokemon Name", "Type"]
table.add_rows([
    ["Pikachu", "Electric"],
    ["Squirtle", "Water"],
    ["Charmander", "Fire"],
])
table.align = "l"
print(table)
