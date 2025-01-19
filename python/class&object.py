
'''
* Python classes / objects 

* Pyhton is an object orineted programming language
* almost everything in python is an object, with its  properties and methods 
*  a class is like an object constructor or a blueprint for creating objects 



'''


# create a class to create a class, use the keyword class:

class myClass:
    x = 5

#create object : we can use the class named myclasss to create objects
# create an object named p1

p1 =myClass()
print(p1.x)    


'''
*  All classes have a function called __init__(), which is always executed when class is
being initited

* use the __init__() function to assign values to object properties, or  other operations that are necessary to do when the  objects is being created 

'''

class Person:
    def __init__(self,name,age):
        self.name = name
        self.age = age
    
p1 = Person("Ajay",22)
print(p1)




class Person:
    def __init__(self, name,age):
        self.name = name
        self.age = age

    def myfunc(self):
        print(f"hello my name is {self.name} !!")

p1 =  Person("Ajay",22)
p1.myfunc()        


'''


'''        