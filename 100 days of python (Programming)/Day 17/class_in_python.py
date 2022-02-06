
# creating a class

# initialize - to set (variables, counters, switches, etc.) to their starting values at the beginning of a program or subprogram.
# empty class or function can be used with pass
class User:
    def __init__(self, user_id, username):
        # __init__ holds the attributes
        self.id = user_id
        self.username = username
        self.followers = 0
        self.following = 0
        # print("New user being created.")

    def follow(self, user):
        user.followers += 1
        self.following += 1


user_1 = User("001", "Angela")
user_2 = User("002", "Jack")
print(f"User 1 ID: {user_1.id}")
print(f"User 1 username: {user_1.username}")
print(f"User 1 followers: {user_1.followers}")
print(f"User 1 following: {user_1.following}")
print(f"User 2 ID: {user_2.id}")
print(f"User 2 username: {user_2.username}")
print(f"User 2 followers: {user_2.followers}")
print(f"User 2 following: {user_2.following}")
user_1.follow(user_2)
print(f"User 1 followers: {user_1.followers}")
print(f"User 1 following: {user_1.following}")
print(f"User 2 followers: {user_2.followers}")
print(f"User 2 following: {user_2.following}")
print("Hello World")
