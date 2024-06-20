# Code with Harry
    # Decorators are used to modify Functions
# decorators are used to change the behaviour of the existing fuction
'''
def div(a,b):
    print(a/b)

def smart_div(func):
    
    def inner(a,b):
        if a<b:
            a,b = b,a
        return func(a,b)
    return inner


div = smart_div(div)
div(2,4)
'''




'''
def greet(func):                                    # ek fuction banaya greet ka uske andar ek aur function banaya aur main func usme hi call kar diya 
    def mfunc(*args,**kwargs):                      # used for unlimited arguments
        print("Good Morning")
        func(*args,**kwargs)
        print("Thanks for using this function")
    return mfunc

@greet                                            # main upper function
def hello():
    print("hello world")
@greet
def add(a,b):
    print(a+b)

hello()
add(1,2)
'''




# 1 Timing Function DEcorator
    # Write a decoratorthat measures a time afunction taes to execute
'''
import time

def timer(func):
    def wrapper(*args,**kwargs):
        start = time.time()
        func(*args,**kwargs)
        end = time.time()
        print(f"{func.__name__} ran in {end-start} time")
            
    return wrapper

@timer
def example_function(n):
    time.sleep(n)                                    # gives output after how much time is given i.e given 2 seconds

example_function(2)
'''





# 2 Debugging Function call
    # Create a decorator to print a function name and the values of its arguments every time the function is called
'''
def debug(func):
    def wrapper(*args,**kwargs):
        args_value = ', '.join(str(arg) for arg in args)
        kwargs_value = ', '.join(f"{k}={v}" for k, v in kwargs.items())
        print(f"Calling : {func.__name__} with args {args_value} and kwargs {kwargs_value}")                   #func.__name__ is used to give function name i.e greet
        func(*args,**kwargs)
    return wrapper


@debug
def hello():
    print("hello")

@debug
def greet(name, greeting = "Hello"):
    print(f"{greeting},{name}")

hello()
greet("chai", greeting="hanji")
'''





# 3 Cache return values 
    # Implement the decorators that caches the return values of a function,so that when its called with the same arguements , the cached value is return instead of re-executing the function.

import time 

def cache(func):
    cache_value = {}
    print(cache_value)
    def wrapper(*args):
        if args in cache_value:
            return cache_value[args]
        result=func(*args)
        cache_value[args] = result
        return result
    return wrapper

@cache
def long_running_function(a,b):
    time.sleep(4)
    return a + b


print(long_running_function(2,3))
print(long_running_function(2,3))
print(long_running_function(4,3))