# 1 Counting Positive Numbers
   # Give the list of numbers , count how many are positive
       # numbers = [1,-2,3,-4,5,6,-7,-8,9,10]
'''
numbers = [1,-2,3,-4,5,6,-7,-8,9,10]
print(" list is: ", numbers)
positive_number_count = 0

for num in numbers:
   if num>0:
      positive_number_count =positive_number_count + 1    # or # positive_number_count += 1
print("final count of Positive numbers : ",positive_number_count)
'''


# 2 Sum of even numbers
   # calculate the sum of numbers upto given numbers n
'''
n = int(input("Enter the number: "))
sum_even=0
for i in range(0,n):
   if i%2 == 0:
      sum_even = sum_even +1    # or # sum_even += 1
print(sum_even)
'''


# 3 Multiplication table printer 
   # Print a multiplication table for a given number upto 10 , but skip the fifth iteration
'''
number = int(input("Enter the number: "))

for i in range(1,11):
     if i == 5:
        continue                                      # use to skip that iteration
     print(number , 'X' , i , '=' , number* i)
'''



# 4 Reverse a string
     # reverse a string using loop
'''
input_str = str(input("Enter a string: "))
reverse_str = ""
for char in input_str:
    reverse_str = char + reverse_str
print(reverse_str)
'''



# 5 Find the First Non-Repeated Character
    #Given the string, Find the first non-repeated character.
'''
input_str = str(input("Enter a string: "))

for char in input_str:
    print(char)
    if input_str.count(char) ==1:
        print("Char is: ",char)
        break
'''

# 6 Find factorial of number
'''
num = int(input("Enter the number: "))
factorial =1

while num > 0:
    factorial *= num            ## or # factorial = factorial * num       
    num = num-1
print("Factorial:",factorial)
'''

  

# 7 Validate input
   #keep asking the user for input until they enter a number between 1 to 10.
'''
while True:
    number = int(input("Enetr value b/w 1 and 10 : "))
    if 1<= number <=10:
        print("Thanks")
        break
    else:
        print("Invalid number , try again")
'''



# 8 Prime number checker
    # check if a number is prime
'''
number = int(input("Enter a number: "))

is_prime = True

if number > 1:
    for i in range(2,number):
        if (number%i) == 0:
            is_prime = False
            break
print(is_prime)
'''



# 9 List Uniqueness checker
    # Check if all elements in the list are unique. If a duplicate is found, exit the loop and print the duplicate
'''
items=["apple","banana","orange","apple","mango"]

unique_item = set()

for item in items:
    if item in unique_item:
        print("Duplicate: ",item)
        break
    unique_item.add(item)
'''

# 10 Exponential Backoff
    # Implement an exponential backoff strtergy that doubles the wait time between retries,starting from 1 second , but stop after 5 retries

import time
wait_time = 1
max_retries = 5
attempts = 0

while attempts < max_retries:
    print("Attempts", attempts + 1,"-Wait time", wait_time)
    time.sleep(wait_time)
    wait_time = wait_time *2
    attempts = attempts + 1