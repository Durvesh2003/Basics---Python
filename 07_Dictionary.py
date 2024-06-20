chai_dict = {"masala":"spicy",
             "ginger":"zesty",
             "green":"mild"
             }
print(chai_dict)

              # both key and vles is called item

chai_dict["green"]= "fresh"
print(chai_dict)

for chai in chai_dict:
    print(chai)                         #print only keys

for chai in chai_dict:
    print(chai,chai_dict[chai])         #print keys and values
   
for key , value in chai_dict.items():   # print both keys and values
    print(key,value)

if "masala" in chai_dict:
    print("i have masala chai")
else:
    print("not having")

print(len(chai_dict))                      #used to give length 


chai_dict = {"masala":"spicy",
             "ginger":"zesty",
             "green":"mild"
             }
print(chai_dict)

chai_dict["mint"]= "hot"
print(chai_dict)
print(chai_dict.pop("ginger"))            # gives value of mentioned key and remove it from dictionary
print(chai_dict)
print(chai_dict.popitem())                    # removes last key value of the dictionary
print(chai_dict)
del chai_dict["green"]                     # also used to delete item from dict by givinf key 
print(chai_dict)

chai_dict_copy = chai_dict.copy()         # creates a copy of reference  i.e {'masala':'spicy'}
print(chai_dict_copy)

#  item ke andar item or nested key and value
shop_dict = {
    "chai":{"masala":"spicy","ginger":"zesty"},"tea":{"green":"mild","black":"strong"}
}
print(shop_dict["chai"])
print(shop_dict["chai"]["ginger"])


square_num = {x:x**2 for x in range(6)}
print(square_num)
square_num.clear()
print(square_num)


keys = ["masala","ginger","lemon"]
print(keys)
default_value= "delecious"
new_dict = dict.fromkeys(keys,default_value)      # gives the same value for all keys in list
print(new_dict)