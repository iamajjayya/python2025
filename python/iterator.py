'''

Python Iteraors


An Iterator is an object that contains a countable  number of  values

->  you can travrerse throgh all the values

-> traverse through all the values 
-> iterator is an   object , which implements the  iterator protocol which consist of the  methods

__iter__() and __next__().



Iterator vs Iterable


'''


myTuple = ("apple","bannana","cherry")
myit = iter(myTuple)

print(next(myit))
print(next(myit))
print(next(myit))



class MyNumber:
    def __iter__(self):
        self.a = 1
        return self
    
    def __next__(self):
     if self.a  <= 20:
        x =  self.a
        self.a +=1
        return x
     else :
        raise StopIteration



myclass = MyNumber()
myiter  = iter(myclass)

for x  in myiter:
   print(x)


