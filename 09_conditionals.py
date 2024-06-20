# c0nditionals questions 

# 1 Age group categorization
   #classify a persons age group: child(<13) , Teenager(13-19), Adult(20-59), senior(60+)
'''
age = int(input("Enter the age:"))
if age< 13:
    print("child")
elif age<20 :
   print("Teeneger")
elif age<60:
    print("Adult")
else:
    print("Senior")    
'''


# 2 Movie ticket pricing 
   # Problem:Movie tickets are priced based on age: $12 for Adults(18 an over), $8 for childrens.Everyone gets a $2 discount on wednesday


#age= int(input("Enter the age:"))
#day = str(input("Enter the day:"))
'''
price = 12 if age>= 18 else 8
if day == "Wednesday":
    price=price-2
    # or we can use
    # price -= 2
print(" Ticket price is $",price)    
'''
#or 
'''
if age>=18:
    if day== "Wednesday":
        price = 12-2
        print("Ticket price $",price)
    else:
        price =12
        print("Ticket price $",price)
else:
    if day=="Wednesday":
        price=8-2
        print("Ticket price $",price)
    else:
        price= 12
        print("Ticket price $",price)    
'''


# 3 Grade calculator
   #assign a letter grade based on a student's score: A(90-100), B(80-89), C(70-79), D(60-69), F(below 60)

'''  
score= float(input("Enter the score:"))
if score>=101:
    print("Please verify your grade again")
    exit()  # instead of break
else:
    if score>= 90:
      grade ="A"
    elif score>= 80:
      grade ="B"
    elif score>= 70:
      grade ="C"
    elif score>= 60:
      grade ="D"
    else:
     grade="F"
print("Grade :",grade)
'''


# 5 Fruit Ripeness checker
  #Determine if a fruit is ripe ,overripe or unripe based on its colour.(e.g Banana:Green-unripe,Yellow-ripe, Brown-Overripe)
'''
fruit = str(input("Enter the fruit:"))
color = str(input("enter the colour:"))

if fruit == "banana":
  if color == "green":
    print("fruit is Unripe")
  elif color == "yellow":
    print("fruit is Ripe")
  elif color == "Brown":
    print("fruit is Overripe")
else:
  print("no other fruit then banana exists")
'''


# 6 Weather actitvity suggession
  # suggesst an activity based on weather (e.g. Sunny-Go for a walk,Rainy - Read a book)
'''
weather = str.lower(input("Enter the weather:"))

if weather == "sunny":
  print("Go for a walk")
elif weather == "rainy":
   print("Read a book")
elif weather == "snowy":
  print("Build a snowman")
else:
  print("no weather conditon!!!")
'''


# 6 Transportation mode selection
    # Choose a mode of transportation on the distance (e.g <3 km :walk,3-15 km: Bike,>15 km: car)

'''
distance= int(input("enter the distance in km:"))

if distance< 3 :
  print("do walk")
elif distance <=15:
  print("do use of bike")
elif distance> 15:
  print("do use of car")
else:
  print("no transport")
'''


# 7 coffe Costomization
   # customize a coffe order :"small","medium", or "Large" with an option for "extra sort" of espresso
'''
order = str.lower(input(" enter the order size:"))
extra_shot = True

if extra_shot:
    coffee = order + " coffee with an extra shot"
else:
     coffee = order + " coffee"
print("Order :", coffee)
'''



# 8 Password Strength checker
   # cheak if a password is "weak","medium",or "strong". Criteria: < 6 chars(weak), 6-10 chars(medium), >10 chars (Strong). 
'''
password = str(input("Enter the password : "))

if len(password) < 6:
    print("weak password")
elif len(password) <=10:
    print("medium password")
elif len(password) > 10:
    print("strong password")
'''



# 9 Leap Year Cheaker
   # determine if year is a leap year .(leap years are divisible by 4 , but not by  100 unless also divisible by 100)
'''
year = int(input("enter the year: "))

if (year%4 ==0 and year%100 != 0) or(year%400 == 0):
    print(year," is leap year")
else:
    print(year ,"is not leap year")
'''



# 10 Pet Food recomendation
    # recommend a type of pet food based on the pets species and age.(e.g Dog < 2 years-Puppy food, Cat:>5 years - SEnior cat food)

years = int(input("enter the year:"))
species = str.lower((input("enter the species:")))

if species == "dog":
    if years <2:
        print(species ," should have puppy food")
    else :
        print(species,"have no specified food")
elif species == "cat":
    if years >5:
        print(species,"should have senior cat food")
    else:
         print(species," have no specified food")  
else:
    print("no other species" )