# 7.Write a Python program to find Anagram Check?

S1 = str(input("Enter a string 1 :"))
S2 = str(input("Enter a string 2 :"))
S1.lower()
S2.lower()
def angram():
    for char in S1:
        if char in S2:
            print ("Angram")
            break
        else:
            print("not Angram")
            break
angram()
