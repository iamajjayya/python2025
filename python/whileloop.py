'''

Python has two primitive loop commands:

*  while loops
* for loops

'''

'''

*  while loop : with the while loop we can execute a set a statement as long as a  conditon is  true

'''

i = 1
while  i < 6:
    print(i)
    i+=1


'''
*  break  statement  we can stop the  loop even if  the while condition is  true:
'''    

i=1
while i < 6:
    i += 1
    if i==3:
        continue
    print(i)

    