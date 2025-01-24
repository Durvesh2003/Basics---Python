# 15.Write a Python program to calculate Factorial without Recursion?

num = int(input("enter a number: "))
fact = 1
if num< 0 :
    print("invlid number")
elif num == 0:
    print("Factorial of 0 is 1")
else:
    for i in range(1,num+1):
        fact = fact*i
    print(f"Factorial of {num} is {fact}")
