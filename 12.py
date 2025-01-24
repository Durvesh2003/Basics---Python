# 12.Write a Python program to calculate Sum of Digits in a Number?
number = int(input("enter a number:"))
num_digit = abs(number)
digits = str(num_digit)
total = 0
for digit in digits:
       total += int(digit)
print(f"The sum of the {number} is {total}")
