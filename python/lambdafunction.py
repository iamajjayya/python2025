'''

*  A lambda function is a small anonymous function
*  A lambda function can take any number of arguments, but can only have one expression

Syntax 

lambda arguments :  expression  
'''


x =  lambda a , b: a+10+b
print(x(5,6))


def myfunction(n):
    return lambda a :  a * n

mydoubler  = myfunction(2)
print(mydoubler(11))