

class User:
    def __init__(self, name):
        self.name = name
        self.is_logged_in = False
    
# Day 27 unlimited positional arguments (args) and keyword arguments(kwargs)
def is_authenticated_decorator(function):
    def wrapper(*args, **kwargs):
        if args[0].is_logged_in == True:
            function(args[0])
    return wrapper

@is_authenticated_decorator
def create_blog_post(user):
    print(f"This is {user.name}'s new blog post.")

# new_user = User("Angela")
# new_user.is_logged_in = True
# create_blog_post(new_user)

'''Create a logging_decorator() which is going to log the name of the 
function that was called, the arguments it was given and finally the 
returned output.'''
def logging_decorator(fn):
    def wrapper(*args, **kwargs):
        print(f"You called {fn.__name__}{args}")
        result = fn(args[0], args[1], args[2])
        print(f"It returned: {result}")
    return wrapper


@logging_decorator
def a_function(a, b, c):
    return a * b * c
    
a_function(1, 2, 3)