'''
A class is a  blueprint for creating objects, an objet is an instance  of a  class 

Syntax


class className:
  def __init__(self, attributes)

 #initialize attributes
    self.attribute  = attributes

  def method(self):

  #perform some action
  pass  

 
'''


#class

class Car:
    def __init__(self,brand,model):
        self.brand = brand
        self.model = model
   
    def start(self):
        return f"{self.brand} {self.model} is strating"
    
# create an object 
car  = Car("Toyota","Corolla") 
print(car.start())       
    


