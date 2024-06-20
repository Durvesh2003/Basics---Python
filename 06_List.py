#---------------------lists---------------------------------

tea_varieties = ["Black", "Green", "Oolong", "White"]
print(tea_varieties)
print(tea_varieties[1])
print(tea_varieties[-1])
print(tea_varieties[:])            # slicing
print(tea_varieties[:2])           # slicing
print(tea_varieties[1:3])          # slicing

tea_varieties[3] = "herbal"        # third index is change from white to herbal
print(tea_varieties)

  # replacing
tea_varieties = ["Black", "Green", "Oolong", "White"]
tea_varieties[1:2] = "Lemon"                                           # string is treated like a array and all letters are separted individual
print(tea_varieties)

tea_varieties = ["Black", "Green", "Oolong", "White"]         
tea_varieties[1:2] = ["Lemon"]                                         # since square bracket is added the whole sting is added in list see in o/p to get more understandable
print(tea_varieties)

tea_varieties = ["Black", "Green", "Oolong", "White"]  
tea_varieties[1:3]= ["Lemon" , "Masala"]
print(tea_varieties)

tea_varieties = ["Black", "Green", "Oolong", "White"]  
print(tea_varieties[1:1])                                         # gives empty list

tea_varieties[1:1] = ["test", "test"]
print(tea_varieties)

print(tea_varieties[1:3])

tea_varieties[1:3] = []                                           # we converted [1:3] index to empty
print(tea_varieties)



#-----conditional statements ------

tea_varieties = ["Black", "Green", "Masala", "White"]
for tea in tea_varieties[0:3:2]:
    print(tea)
   

'''tea_varieties = ["Black", "Green", "Masala", "White"]
for tea in tea_varieties:
    print(tea, end="-")'''


tea_varieties = ["Black", "Green", "Masala", "White"]
#if "Oolong" in tea_varieties:
#    print("we have Oolong tea")                                  # Oolong is no present list so it will not print
tea_varieties.append("Oolong")                                    # used add values at end of the list
print(tea_varieties)
#if "Oolong" in tea_varieties:
#    print("we have Oolong tea")  
tea_varieties = ["Black", "Green", "Masala", "White"]            # used to popvalues from list with helpof index if we does not specify any index it will automatically pop the last element/value of list
print(tea_varieties.pop())

tea_varieties = ["Black", "Green", "Masala", "White"]            # used to remove value from list by specifing the value
tea_varieties.remove("Black")
print(tea_varieties)    

tea_varieties = ["Black", "Green", "Masala", "White"]            # used to insert values by giving index and values 
tea_varieties.insert(1,"Lemon")
print(tea_varieties)

tea_varieties = ["Black", "Green", "Masala", "White"] 
tea_varieties_copy = tea_varieties.copy()                        # used to copy reference which is a copy and not reference
print(tea_varieties_copy)
tea_varieties_copy.append("Lemon")
print(tea_varieties)
print(tea_varieties_copy)


squard_num = [x**2 for x in range(10)]
print(squard_num)

cube_num = [x**3 for x in range(5)]
print(cube_num)
