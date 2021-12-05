print("------------------------------step1------------------------------")

name = "OSM"
age = 21
print(name+":")
#print(type(name))
#print(type(age))

frist_name="ali"
last_name="habibi"
full_name=frist_name+" "+last_name
#print("Hello "+full_name+"!!!")

numbr = 13
numbr=numbr+1
#or
numbr +=1
#print(numbr)
print("your age is: "+str(numbr))

height = 36.56
#print(height)
#print(type(height))
print("Your height is: "+str(height)+"cm")

human = True
huwoman = False
print("Are you a human: "+str(human))
print(human+huwoman)
print(type(human))

print("------------------------------step2------------------------------")

#multiple
#int1 = 30
#int10 = 30
#int100 = 30

int1=int10=int100=30

print(int1)
print(int10)
print(int100)

print("------------------------------step3------------------------------")

name="osm m12"

# tedad horof + spayci
print(len(name))
# ebarat
print(name.find("s"))
# captal
print(name.capitalize())
# big
print(name.upper())
# smal
print(name.lower())
# adad123...
print(name.isdigit())
# spase remov
print(name.isalpha())
# tedad har harf dar string
print(name.count("m"))
# jabe ja kardan harf dar str
print(name.replace("m","v"))
# span
print(name*3)

print("------------------------------step4------------------------------")

x = 1
y = 13.0
z = "3"

x = str(x)
y = int(y)
z = float(z)

print("x is: " +  x)
print(y)
print(z*3)

print("------------------------------step5------------------------------")

name5 = input("What is your name? ")
age5= int(input("How old are you? "))
height5= float(input("How tall are you? "))

#age5 = age5+1

print("Whelcom " + name5)
print("You are "+str(age5)+" years old")
print("You are "+str(height5)+"cm tall")

print("------------------------------step6------------------------------")

import math

pi = 3.5
x6 = 1
y6 = 2
z6 = 3

# rond mokone
print(round(pi))
# bishtar az 0.0000000000000001 be adad ezafe beshe mire adad badi!
print(math.ceil(pi))
# none!!!
print(math.floor(pi))
# meghdar manfi ro mosbat mikone
print(abs(pi))
# tavan mide be adad
print(pow(pi,2))
# none!!!
print(math.sqrt(10))
# bala tarin meghdar
print(max(x6,y6,z6,pi))
# paein tarin meghdar
print(min(x6,y6,z6,pi))

print("------------------------------step7------------------------------")

name7="osm code"

# [start:stop:step]

first_name7 = name7[:3]
# [mitoni 0 nazari!:stop:step]
last_name7 = name7[4:]
funky_name7 = name7[::2]
reversed_name7 = name7[::-1]

print(reversed_name7)

website1 = "https://google.com"
website2 = "https://wikipedia.com"

slice = slice(8,-4)

print(website1[slice])
print(website2[slice])

print("------------------------------step8------------------------------")

# video time => 00:52:13
age8 = int(input("How old are you? "))

if age8 == 100:
    print("You are a century old!")
elif age8 >= 18:
    print("You are an adult!")
elif age8 < 0:
    print("You haven`t been born yet!")
else:
    print("You are child!")

print("------------------------------step9------------------------------")

# video time => 00:58:50

temp = int(input("What is the temporature outside? "))
# and or not
# and = beyn do shart
# or = harchi birone sharte
# not = manfi mikone sharto =>if not(shart):
if temp >= 0 and temp <= 30:
    print("the temporature is good today")
    print("go outside!")
elif temp >= 0 or temp <= 30:
    print("the temporature is bad today")
    print("stay inside!")

print("------------------------------step10------------------------------")

# video time => 01:04:15

starter = False
while starter:
    print("iam loop")

name10 = None
while not name10:
    name10 = input("Enter your name: ")
print("Hello " + name10)

print("------------------------------step11------------------------------")
