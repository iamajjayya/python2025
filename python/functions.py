'''

A function is a block of code which only runs when it is called 

pass data, known as parameters, into a function.

a function can return  data as a result 

'''

#creating a function 

def my_function():
    print(" Hello from a function ")

#Calling a function 

def my_function1(fname):
    print(fname + " Refsne")

my_function1("Ajay")   


def example_fun(*kids):
    print(" The Youngest child is" + kids[0])

example_fun("Emil","Tobias","Linus")



def tri_recursion(k):
  if(k > 0):
    result = k + tri_recursion(k - 1)
    print(result)
  else:
    result = 0
  return result

print("Recursion Example Results:")
tri_recursion(6)



def tri(k):
   if(k > 0):
      result  =  k + tri(k-1)
      print(result)
   else:
      result = 0
   return result

