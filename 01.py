# 1.Write a Python program to Reverse a String?

input_string = str(input("Enter the string:"))
reversed_string = ""

for char in input_string:
    reversed_string = char + reversed_string

print("Original string:",input_string)
print("Reversed_string is:",reversed_string)