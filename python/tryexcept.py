'''

The try - block lets you test  block of   code for errors

except - block lets you handle the  error 

else -  block lets you execute  code  when there is  no error 

finally - block lets  you execute code, regardless of  the result of  the  try and except blocks


Exception Handling 


When an error occurs or exception as we call it , python will normally stop and  generate  an error message 



'''


try:
    x = "now x is defined"
    print(x) # x is  not defined 
except:
    print("An exception occured")    

try:
    print(Z)
except NameError:
    print(" variable y is not defined") 
except :
    print(" Something else went wrong")


try:
    print("Hello")
except: 
    print("something went  wrong")
else :
    print("Nothing  went  wrong")            


try:
    print(a)
except:
    print("Something went wrong")
finally:
    print(" The try except is finished")


try:
    f  = open("pip.py")
    try:
        f.write(" Hello ")
    except:
        print(" something went  wrong when writing to the  file")
    finally:
        f.close()
except:
    print("Something went wrong when opening the file")        



x  = -1

if x < 0:
    raise Exception(" sorry  , no numbers  below zero")


x  = "hello"

if not type(x) is int:
    raise TypeError(" Only Integers are allowed")
