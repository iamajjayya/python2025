'''
Python Polymorphism


Polymorphism means "many forms" and in  programming it refres to methods/functions/operators with the same name that can be executed on many objects or classes

Function Polymorphism 


An example of a  python  function that can be used on different objects  is  the  len() function


'''

'''

Class Polymorphism 

Polymorphism is often used in class methods, where wwe can have multiple  classes with the same method  name.

'''

class Car:
    def __init__(self, brand,model):
        self.brand  = brand
        self.model = model

    def  move(self):
        print("Drive!")

class Boat:
    def __init__(self, brand,model):
        self.brand  = brand
        self.model = model

    def  move(self):
        print("Sail!")

class Plane:
    def __init__(self, brand,model):
        self.brand  = brand
        self.model = model

    def  move(self):
        print("Fly!")                    
    
car1 =  Car("Ford","Mustang")
boat1 = Boat("Ibiza","Touring 20")
plane1 = Plane("Boeing","747") 

for x  in (car1,boat1,plane1):
    x.move()