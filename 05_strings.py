str1 = "Masala chai"
first_character = str1[0]
print(first_character)               # first char
print(str1[0])
slice_str1 = str1[0:6]
print(slice_str1)                    # slicing
print(str1[0:6])


#slicing in strings
num_list = "0123456789"
print(num_list[ : ])
print(num_list[3: ])
print(num_list[ :7])
print(num_list[0:7:2])            # 0 means starting ,7 mens ending , 2 means diffference
print(num_list[0:7:2])  
print(num_list[0:-1:2])  

name = "Durvesh Kadave"
print(name.lower())                                 # lower i.e all the words arein lowercase
print(name.capitalize())                            # starting letter of word is captilaze
print(name.upper())                                 # sting is converted in uppercase
print(name.replace("Durvesh","Mayuresh" ))          # replace the words of string

chai = " lemon, ginger, masala, mint , masala"
print(chai.split())
print(chai.split(",  "))
print(chai.find("lemon"))
print(chai.count("masala"))

chai_type = "masala"
quantity = 2
order = " I ordered {} cups of {} chai"
print(order.format(quantity,chai_type))
print(len(chai_type))

chai_variety = ["lemon","masala","ginger"]
print("".join(chai_variety))
print(" ".join(chai_variety))
print("-".join(chai_variety))
print(", ".join(chai_variety))

chai1 = "Masala chai"
for letter in chai1:
    print(letter)
    
chai2 = "Masala\nchai"
print(chai2)
    
chai3 = r"Masala\nchai"
print(chai3)