# 13.Write a Python program to check for Armstrong Number?
number = int(input("Enter a number: "))
digits = str(number)
num_digit = len(digits)
total = 0
for digit in digits:
    total += int(digit)**num_digit
if total == number:
    print("Armstong")
else:
    print("not armstrong")

