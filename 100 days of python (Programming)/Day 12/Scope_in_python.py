#  -----------------------               !!!!! SCOPE !!!!!                ------------------------- #

# enemies = 1
# def increase_enemies():
#     enemies = 2
#     print(f"enemies inside function: {enemies}")
#
# increase_enemies()
# print(f"enemies outside function: {enemies}")

# !!!!! ----- LOCAL SCOPE ----- !!!!! #

# def drink_potion():
#     potion_strength = 2
#     print(potion_strength)
#
# drink_potion()
# print(potion_strength)      #  this line gives : NameError: name 'potion_strength' is not defined because it is outside the function


# !!!!! ----- GLOBAL SCOPE ----- !!!!! #

# player_health = 10
# def drink_potion():
#     potion_strength = 2
#     print(player_health)
#
# drink_potion()
# print(player_health)

#       There is no Block Scope in Python👎 like C/C++👍 , Java👍.


#                   MODIFYING GLOBAL SCOPE
#       WARNING:- Never try to Modify the Global Scope as it is highly prone for bugs

# enemies = 1
# def increase_enemies():
#     global enemies
#     enemies += 1
#     print(f"enemies inside function: {enemies}")
#
# increase_enemies()
# print(f"enemies outside function: {enemies}")

# another way

# enemies = 1
# def increase_enemies():
#     print(f"enemies inside function: {enemies}")
#     return enemies + 1
#
# enemies = increase_enemies()
# print(f"enemies outside function: {enemies}")

#               GLOBAL CONSTANTS

# PI = 3.14159
# URL = "www.globalpython.org"


