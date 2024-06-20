T1= ("black","green","yellow")
print(T1)
print(T1[0])
print(T1[-1])
print(T1[1:])
print(T1[0])

# T1[0]="blue"                        # since tuple are immutable they cannot me changed o this will not work
# print(T1)

print(len(T1))

T2 = ("green","purple","orange")
T3 = T1 +T2
print(T3)

if"green" in T1:
    print("it is present")


T2 = ("green","purple","orange","blue","white","green")
print(T2.count("green"))


T4= ("Black","Blue")
(black,blue)=T4
print(black)

# there is also nesting in tuple
T5 = ("hello",(1,2,3),"Bye")
print(T5)