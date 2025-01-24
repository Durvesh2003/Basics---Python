# 8. Write a Python program to find Prime Numbers?
num = int(input("enter a number : "))
if num<2:
        print("not prime")
        
else:
    for i in range(2,num):
        if num % i == 0:
            print("not prime number")
            break
    else:
            print("Prime number")
            