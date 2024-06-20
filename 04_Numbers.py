'''
x = 2
y = 3
z = 4
print(x+y)
print((x + y) * z)
f = int(3.14)
g = float(2.44)
print(x + f + g)
print(y%2)                  # it gives remainder
print(z**2, z**5)
print((x,y,z))

print(repr('chai'))
print(str("chai"))         # all three repe, str,print are different
print('chai')

#comparision operators       gives true or false
print(x<y)
print(x == y)          
print(y>z)
print(x<y and x<y)          # in and it is true if both the conditions are satiesfied
print(x<y and x>y)
print(x<y or x>y)           # in or it is true if one of the condition is satiesfied
                            # 1 = TRUE and 0 = FALSE
print (1 == (y<z))          # here 1 means true
print (0 ==(x<z))
'''





# in terminal
'''
>>> import math
>>> math.floor(3.5)               #floor is used to print previous number
3
>>> math.floor(-3.5)
-4
>>> math.floor(3.9)  
3
>>> math.floor(3.6) 
3
>>> math.trunc(2.8)              # trunc is ued to give nearest number to 0
2
>>> math.trunc(-2.8)
-2
>>> math.trunc(8.3)  
8
>>>
'''






'''
print(0o20)                      #print octel numbers
print(0xFF)                      #print hexadecimals numbers
print(0b1000)                    #print binary numbers
print(oct(64))                   #converting number into octel
print(hex(64))                   #converting number into hexa
print(bin(64))                   #converting number into binary

# onother method for converting the numbers in octel,hexa,binary
print(int('64',8))
print(int('64',16))
print(int('10000',2))
'''







# in terminal use of random library
'''
>>> import random
>>> list = ['lemon','ginger','masala','mint']
>>> random.choice(list)                             # random makkes own choice
'masala'
>>>
>>> random.choice(list)
'lemon'
>>> random.choice(list)
'lemon'
>>> random.choice(list)
'ginger'
>>> random.shuffle(list)                              # random shuffles the list its own 
>>> list
['lemon', 'ginger', 'masala', 'mint']
>>> random.shuffle(list)
>>> list
['masala', 'lemon', 'ginger', 'mint']
>>>
'''






#sets

setone = {1,2,3,4}
settwo = {1,3,7}
print(setone & settwo)               # intersection(& symbol is used)    same vales print
print(setone | settwo)               # union (| symbol is used)          all vlues print single time(unique values)
print(setone - settwo)               #subtraction
print(setone - {1,2,3,4})            #subtraction  only subtraction allowed

