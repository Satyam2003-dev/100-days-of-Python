
'''Python functions as First Class Objects: Passing & Nesting Functions'''

'''functions can have inputs'functionality/output'''
# def add(n1, n2):
#     return n1+n2

# def subtract(n1, n2):
#     return n1 - n2

# def multiply(n1, n2):
#     return n1*n2

# def divide(n1, n2):
#     return n1/n2

'''Functions are first-class objects, can be passed around as arguments '''
# def calculate(calc_function, n1, n2):
#     return calc_function(n1,n2)

# result = calculate(multiply, 2, 3)
# print(result)

'''Functions can be returned from other functions'''
# def outer_function():
#     print("I'm outer")
#     def nested_function():
#         print("I'm inner")
#     return nested_function
# inner_function = outer_function()
# # inner_function()
# inner_function

'''Python Decorator Function'''
import time

def delay_decorator(function):
    def wrapper_function():
        time.sleep(2)
        function()
        function()
    return wrapper_function

#@function_name known as syntactic sugar
@delay_decorator
def say_hello():
    print("Hello")

@delay_decorator
def say_bye():
    print("Bye")


def say_greeting():
    print("How are you?")

# doesn't get triggered immediately
say_hello()

# alternate way without using syntactic sugar
decorated_function = delay_decorator(say_greeting)
decorated_function()