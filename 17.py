# 17.Write a Python program to Remove Duplicates from a String?
str1 = str(input("enter a string: "))
str1.lower()
required_string = ""
for char in str1:
    if char not in required_string:
        required_string += char
print(" required string is : ", required_string)


