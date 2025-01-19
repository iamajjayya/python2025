#Variables

#Variables are container  for storig data values

#Creating Variables

#Python has no command for declaring a variables 
#A variables is created  the moment you first assign a value to it 

#Casting
#If  u want to specify the data  type of a variable, this can be done with casting

x = str(3)
y = int(3)
x = float(3)



#get the type
# You can get the data type of a varible with the type() function

#example 
x=5
y="john"

print(type(x))
print(type(y))


#unpack a colletion

#if  u have a collection of values in a list, tuple etc,  python allows you to exraxt the values  into variables , Thos is called unpacking
# 
# 
fruits = ["apple","bannana","cherry"]
x,y,z =  fruits
print(x)
print(y)
print(z)
 