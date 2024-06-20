# 1 Basic function program 
   # Write a function to calculate and return the square of a number
"""
def square_of_num(number):
      return number**2

print(square_of_num(4))
"""




# 2 functions with multipie parametrers
    # create a functions that takes two numbers as parameters and returns their sums
'''
def sum(a,b):
    return a + b

print("Sum is :",sum(10,20))
'''



# 3 Polymorphism in functions 
    # write a function multiply that multiplies two numbers , but can also accept and multiply strings.
'''
def multiply(num1 , num2 ):
    return num1 * num2

print(multiply( 5, 4))
print(multiply(5, 'h'))
print(multiply( 'a', 4))
'''




# 4 Function returning multiple values
    # creates a function thst returns both the area and the circumference of circle given its radius.
'''
import math          # used for getting pi value

def circle_stat(radius):
    circle = math.pi * (radius ** 2) 
    circumferenc = 2 * math.pi * radius
    return circle, circumferenc

a , c = circle_stat(3)

print( "area :", a ,"\ncircumference : ", c)
'''




# 5 Default parameter value 
   # write a functions that greets a user. If no name is provided , it should greet with a default name
'''
def greet(name = "User"):
    return "Hello,"  + name + " !"

print(greet("Prasad"))                      # if value is given then it will use that value i.e Prasad
print(greet())                              # if value is not given then it will use default value i.e User
'''




# 6 Lambda Functions
    # create a ambda function to compute the cube of a number
'''
cube = lambda x: x ** 3                # used for chotisi cheeze and small work        # importantly used in labraries in framewoek like flask,django

print(cube(3))
'''



# 7 Functoins with *args
    # Write a function that takes variable number of arguements and returns their sum.
'''
def sum_all(*args):                    #  Aestrig(*) is used to print multiple argument
    print(args)                        # prints values in tuple (1,2,3)  and we can iterate it using loop
    #print(*args)                       # print values normal 1,2,3   and we cannot iterate it using loop
    for i in args:
        print(i*2)
    return sum(args)                   # sum() is default method to print sum

print(sum_all(1,2,3))
print(sum_all(1,2,3,4,5))
print(sum_all(1,2,3,4,5,6,7,8))
'''




# 8 Function with **kwargs
     # create a functions that accpth any number of key word arguments  and printts them in a format  key:value
'''
def print_kwargs(**kwargs):
    for key,value in kwargs.items():
        print(f"{key}:{value}")
print_kwargs(name = "shaktiman",power ="lazer")
print_kwargs(name = "shaktiman")
print_kwargs(name = "shaktiman",power ="lazer", enemy = "Dr. Jackaal")
'''




# 9 Generator function with yield
    # Write a Generator functions that yields even numbers upto a specified limit.
'''
def even_generator(limit):
    for i in range(2,limit+1,2):
        yield i                              # yield is also used to return value but memory ko oos funcion mai rakhta hai and state ko bhi rakhta hai

for num in even_generator(10):
    print(num)
'''




# Recursive Function
    # Create a recursive function to calculate factorial of number

def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n- 1)

print(factorial(4))
        