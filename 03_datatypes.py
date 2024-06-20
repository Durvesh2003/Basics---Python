#types of data types / object types 
   # Numbers(num) : 1234 ,3.143 ,3+4j ,0b111 , decimal() , fraction()
   # strings(str) : 'hello' , "byeee" , b'a\x01c' , u'sp\xc4m' 
   # list : [1, 2],[1,[2,'three'],4,5], list(range(10))
   # tuple : (1, 'spam', 4 , 'U'), tuple('spam'), nametuple
   # Dictionaries(dict) : {'food': 'ice-cream,, 'taste': 'yummy' , 'cost': 100 }                                                      note- dict never starts from zero
   # set : set('abc'), {'a','b','c'}
   # File : open('eggs.txt'), open('C:\ham.bin', 'wb')
   # Boolean : True, False
   # None : None
   # integers and Float
   # Functions, classes, modules

   # Advanced : Decorators , generators , Iterators, MetaProgramming




#----------------list------------------           operations used are all built-in functions in list
'''
print(["list metods"])
L1=[1, "hi", "bro", 22 , "ace","hi"]
L2=['abc','xyz', 24]
print(L1)
print(L2)
L1.append("ace")                    # used to add the value(ace) in the list at the end
print(L1)
e = L1.count("ace")
print("numbers of ace in list are:",e)      # used to count number of ace int the list
L2.extend([1,2,3])                          # used for extending the list or adding at the last of the list
print("List after extending:",L2)          
L2.insert(2,33)                              # used for inserting values(string,int,etc) by giving the index first and then values
print("list after the insertion:",L2 )
L2.pop(1)                                     # used popping the value from list by giving the index 
print("list after the popping:",L2 )        
L1.remove("hi")                               # used for deleting the value my mentioning it only once.
print("list after the deletion:",L1 )   
L2.reverse()                                  # used to revers the list
print("list after the reversing:",L2 )
L3 = [1,23,8,45,26,16]
print("the list is",L3)
L3.sort()                                     # used for sorting the list
print("after sorting list:",L3)
S = sum(L3)                                   # used for finding he sum of list
print("sum of list:", S)
print("Max=",max(L3))                         # used to find the maximum value of list
print("Min=",min(L3))                         # used to find the minimum value of list
L3.clear()                                    # used to clear the list or empty whole list 
print("After clearing the list",L3)
'''




#--------------Tuple-------------------------      operations used are all built-in functions in Tuple

'''
print("Tuple methods")
T1 = (1,2,3,4)
T2 = (1,'abc','xyz',4)
print(T1)
print(T2)
T3 = T1 + T2                                 # merging two tuples
print("Merge two tuples",T3)
print("Max =",max(T1))                       # used to print max value for tuple and tuple should contain only numbers only
print("Min =",min(T1))                       # gives min value and tuple should contain only numbers only
print("strin of T3",T1[1:6])                 #used to print string from this to this index and tuple should contain only numbers only
print("length of the tupl",len(T1))          # used to give length of tuple
L4 = [1,2,3,4,'hello']
print(L4)
T4 = tuple(L4)                                    # used for converting list to tuple
print("after converting list into tuple:", T4)
print("number of 1 in count:",T3.count(1))        # used for counting number of 1 in tuple
T5 = (34,23,4,21,45,11,47)
print("Tuple before sorting :", T5)
print("Tuple after sorting:",sorted(T5))          # used for sorting and o/p of sorting comes in square bracket
'''




#--------------------string-------------------------

'''
print("Sring Function")
S1 = 'good morning'
print("S1 is :", S1.capitalize())                 # used to captilize first word of the string-----------o/p Good morning
print("S1 is:", S1.upper())                       # used to write whole string in uppercase/captalize letters----------o/p GOOD MORNING
print("S1 is:",S1.lower())                        # used tonwrite whole string in lowercase letters-------------0/p good morning
print("strings starts with g:",S1.startswith('g',0,7))        # used to check condition is true or not------------true
print("Strings ends with space:",S1.endswith("",18))           # used to check condition is true or not-----------false
S2 = 'Ace'
print("S2 is alphabet:",S2.isalpha())                          # check whether the s2 is alphabet------------true
print("S2 is lower:",S2.islower())                             # check whether the S2 is lower  case or not-----false
S3 = '123'
print("S3 is digit:",S3,S3.isdigit())                          # check s3 is digit or not-----true
print("S3 is lower:",S3.islower())                             # S3 is lower or not  ----false
S4 = ""
print("S4 has space:",S4.isspace())
S5 ="123dft"
print("is S5 has is alnum:",S5.isalnum())                      # check whether S5 has alphabet and numbers-------true
'''




#--------------Sets--------------------

'''
thisset = {"apple","banana","cherry","orange","grapes"}
print(thisset)
thisset = {"apple","banana","cherry","orange","grapes","apple","orange"}    # duplicates are not allowed in sets
print(thisset)
thisset = {"apple","banana","cherry",True, 1 ,2}                            #true and 1 considered as same values in sets and treated as duplicate
print(thisset)
thisset = {"apple","banana","cherry",False,True ,0}                         #false and 0 considered as same values in sets and treated as duplicate
print(thisset)
print(len(thisset))                                                         # used to print length of the sets

set1 ={"apple","banana","cherry"}
set2 =(1,5,7,3,9)
set3 =[True,False,True]
print(type(set1))
print(type(set2))                                           # gives type object type
print(type(set3))

thisset = set(("apple","banana","cherry"))                  # note the double round- brackets
print(thisset)
'''

#sets
'''
setone = {1,2,3,4}
settwo = {1,3,7}
print(setone & settwo)               # intersection(& symbol is used)    same vales print
print(setone | settwo)               # union (| symbol is used)          all vlues print single time(unique values)
print(setone - settwo)               #subtraction
print(setone - {1,2,3,4})            #subtraction  only subtraction allowed
'''

#-------------------Dictionaries-------------------------

'''
thisdict = {                                 #{"key":"values"}
    "brand": "Ford",
    "Model": "Mustang",
    "year": 1964
}
print(thisdict)
print(thisdict["brand"])

thisdict = {
        "brand": "Ford",
    "Model": "Mustang",
    "year": 1964,                   # duplicate values will overwrite exesting values(i.e 2020 will print instead of 1964)
    "year":2020
}
print(thisdict)
print(len(thisdict))                # used to print length of dictionary
print(type(thisdict))               # used to print type 

thisdict = dict(                    #use dict() method to make dictionry
    name = "john",age =36,
    country = "USA"
)
print(thisdict)

thisdict2 ={
    "one":"lemon",
    "two":"ginger",
    "comic":"naagraj"
}
print(thisdict2["comic"])
'''
