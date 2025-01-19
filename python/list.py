#List 

mylist = ["apple,","bannana","cherry"]

'''
Lists are used  to store multiple items  in a  single variable

Lists are  one of 4 built in data  types in python used to store collection of data

'''

print(mylist)

'''
List items are  ordered, changeable  and allow  duplicate values


'''

'''
Python Collections(Arrays)

1. List is a collection which is ordered and changable and Allows Duplicate members 
2. Tuple is a colection which is ordered and unchangeable , allow duplicate members
3. Set is collection which is unorderd, unchangable  and  unindexed, no duplicate  members
4. Dictionry is a collection which is  ordered, and changble ,  no  duplicate members 


'''

thislist =  ["apple","bannana","cherry","orange","kiwi", "mango"]
if "apple"  in thislist:
    print("Yes Apple in the list")

thislist.insert(1,"ajjayya")
print(thislist)

'''
Python  - Add List Items 

Append Items 

tO ADD AN ITEM TO THE END OF THE  LIST, use the append() method 


'''

thislist1  = ["apple","bannana", "cherry"]
i=0
while i < len(thislist1):
  print(thislist1[i])
  i = i + 1

[print(x)  for x in thislist1]

for x  in range(len(thislist1)):
    print(thislist1[x])


'''
Python Remove List Items 

1. the  remove() method removes the specified item
2. the pop() method removes  the specified index
3. del keyword also removes the specified index
4. del keyword can also delete the  list completely 
5. clear() method empties  the list 

the list still remains,  but  it has  no content 
'''

'''
Python -  Loop Lists

Loop Through a list 


'''

fruits = [ "bannana", "cherry" ,"apple", "kiwi" , "mango"]
thislist1.sort(reverse=True)
print(thislist1)





'''newlist = []

for x in fruits:
    if "a" in x:
        newlist.append(x)
print(newlist)  


newlist1 = [x for x in fruits if "c" in x]
print(newlist1)
'''

'''
Python - Sort Lists 

'''

thislistsort = ["orange","mango","kiwi","pineapple","bannana"]
thislistsort.sort(reverse=True)
thislistsortnumeric =  [100,40,23,56,32,10]
thislistsortnumeric.sort(reverse=True)
print(thislistsortnumeric)
print(thislistsort)


'''
Cystomize Sort Function

'''


def myfunc(n):
  return abs(n - 40)

thislistcs =  [100,50,65,82,23]
thislistcs.sort(key=myfunc)
print(thislistcs)

