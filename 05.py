# 5.Write a Python program to find Fibonacci Sequence?

number = int(input("enter a number :"))
a,b = 0,1
count = 0
if number<0:
    print("Enter a positive number :")
elif number == 1:
    print("Fibonnaci sequence of 1 is : 0")
else:
    print ("Fibonnaci Sequence :")
    while count< number:
        print(a, end=' ')
        nth = a + b
        a = b
        b = nth
        count = count + 1
    

