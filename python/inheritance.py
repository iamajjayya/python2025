'''
Python Inheritance

Inheritance allows us to  defince a class that inheits all the methods and  properties from  another class 

parent class: is the class being inherited from , also called base class
child class :  is the class that inherits from another class, also called derived class


'''


'''

Create a  Parent class 

'''


class Person:
    def __init__(self, fname, lname):
        self.firstname =  fname
        self.lastname =  lname

    def  printname(self):
        print(self.firstname, self.lastname)    


# Use the Person class to create an object, and  then execute the printname method  

x = Person("Ajjayya", "G V")    
x.printname()    


''''
Create a  child class

to create aa class thet inhierts the functionality from  another class , send the  parent class as a parameter when creating  the child  class:

'''

class Student(Person):
    pass



x = Student("Jeeven","G V")
x.printname()


''''
Add the __init__() function

the  __init__() function is called automatically every time the class  being used  to create a new object 



'''



class Student(Person):
    def __init__(self, fname, lname,year):
        super().__init__(fname, lname)
        self.gradutionyear = year


    def welcome(self):
        print("Welcome", self.firstname, self.lastname,"to the class of" ,self.gradutionyear)


x = Student("Ajjayya","G V",2022)
x.welcome()