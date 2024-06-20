# username = "chaiaurcode"

# def func():
#     # username = "chai"
#     print(username)

# print(username)
# func()




# x = 99                # x is global
# def func2(y):
#     z = x + y         # x ki value global sai hi lee jayege
#     return z

# result = func2(1)
# print(result)




# x = 99
# def func3():
#     x = 88

# print(x)                # x ki value 99 print karege aur hamne to print function ke pahar keya hai aur func3 ko call kareke print bhi nahi keya




# x = 99
# def func3():
#     global x              # avoid this type of global mechanism
#     x = 12

# func3()
# print(x)


'''
x=99
def f1():
    x = 88                  # agar x =88 comment hota toh print karta 99 
    def f2():
        print(x)
    f2()
f1()
'''




# closure
'''
x = 99
def f1():
    x = 88
    def f2():
        print(x)
    return f2
myResult = f1()
myResult()    
'''


def chaicoder(num):
    def actual(x):
        return x ** num
    return actual

f = chaicoder(2)
g = chaicoder(3)

print(f(3))
print(g(4))
    


