# 14.Write a Python program to check for Leap Year?

Year = int(input("Enter a year:"))
if Year%4 == 0:
    if (Year%100 != 0) or (Year%400 == 0):
        print("Leap Year")
    else:
        print("not leap year")    
else:
    print("not leap year")