# 3.Write a Python progam to print number if vowels in in the input
input_str = str(input("Enter the string:"))
vowels = "aeiou"
vowels_count = 0
input_string = input_str.lower()

for char in input_string:
    if char in vowels:
        vowels_count += 1
print("number of vowels are:", vowels_count)
