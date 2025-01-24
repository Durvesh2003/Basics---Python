# 9.Write a Python program to check for Pangram?

L1 = set('abcdefghijklmnopqrstuvwxyz')
str1 = str(input( "Enter a string :"))
str1.replace(" ", "").lower()
for char in L1:
    if char in str1:
        print("Pangram")
        break
    else:
        print("not Pangram")
        break