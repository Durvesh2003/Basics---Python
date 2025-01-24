# 18.Write a Python program to Check for Perfect Number?
number = int(input("enter a number: "))
total = 0
for i in range(1,number):
    if number%i == 0:
        total = total + i
        if total == number:
             print("perfect number")
             break

else:
    print(" not perfect number")
        