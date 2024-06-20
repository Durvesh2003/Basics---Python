import time
print("chai is here ")
username = "hitesh"
print(username)




# f = open('11_iteration_tools.py')                    # this is a file
# print(f.readline())
# print(f.readline())
# print(f.readline())
# print(f.readline())
# print(f.readline())
# print(f.readline())




# f = open('11_iteration_tools.py')                   # this is a file
# print(f.__next__())
# print(f.__next__())
# print(f.__next__())
# print(f.__next__())
# print(f.__next__())
# print(f.__next__())




# f = open('11_iteration_tools.py')                 # this is a file                
# while True:
#     line = f.readline()
#     if not line :
#         break
#     print(line, end='')




# for line in open('11_iteration_tools.py'):              
#     print(line, end = '')




# test = "hitesh"
# if not test:
#     print("chai")

# test = ""
# if not test:
#     print("chai")




# mylist = [1,2,3,4]
# I =  iter(mylist)
# print(I)
# print(I.__next__())       # 1
# print(I.__next__())       # 2
# print(I.__next__())       # 3
# print(I.__next__())       # 4
# print(I.__next__())       # it will stop iteration




# f= open('11_iteration_tools.py')            # this is a file
# print(iter(f) is f )                               # this two lines are 
# print(iter(f) is f.__iter__())                     # same for files but different for list


# myNewList = [1,2,3]
# print(iter(myNewList) is myNewList)


# D = {'a':1, 'b':2}
# for key in D.keys():
#     print(key)

# I = iter(D)
# print(I)
# print(I.__next__())                # a
# print(I.__next__())                # b
# print(I.__next__())                # stop iteration




range(5)
R = range(5)
print(R)
I = iter(R)
print(next(I))                   # 0
print(next(I))                   # 1
print(next(I))                   # 2
print(next(I))                   # 3
print(next(I))                   # 4
print(next(I))                    # stop iteration