#  2.Write a Python program to Check Palindrome?
some_input = input("Enter anything:")
processed_string = some_input.replace(" ","").lower()
reversed_input = ""
for char in processed_string:
    reversed_input = char + reversed_input
if processed_string == reversed_input:
       print("it is palindrome")
else:
        print("not palindrome")
