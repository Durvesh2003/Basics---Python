# 4.Write a Python program to find Factorial with Recursion?

def factorial(n):
    if n==0 or n == 1:
        return 1
    else:
       return n* factorial(n-1)
print(factorial(5))