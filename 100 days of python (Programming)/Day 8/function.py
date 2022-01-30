#   ----- Defining Function -----
def greet():
    print("hello")
    print("How do you do?")
    print("Isn't the weather nice today?")
greet()

#   ----- Function that allow input also -----

def greet_with_name(name):
    print(f"hello {name}")
    print(f"how are you {name}?")
    print(f"{name} isn't the weather nice today?")
greet_with_name("Your name")

#   ----- Function that allow more than one input -----

def greet_with(name, location):
    print(f"hello {name}")
    print(f"how it is in {location}")
greet_with("Harry", "Hogwarts")

#   ----- Other Method -----
greet_with(name="Peter", location="Neverland")
greet_with(location="Neverland", name="Peter")
