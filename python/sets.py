#set

'''
set are used to store multiple items in a  single variable 
set is a collection which is  unordered, unchangeable  and unindexed 

*Note: set items are unchangeable but you can remove items and  new items 

'''



thisisset = {"apple", "bannana", "cherry"}
print(thisisset)
print(len(thisisset))

#Set Items  -  Data Types

print(type(thisisset))
for x in thisisset:
    print(x)


thisisset.add("orange")
print(thisisset)

anotherset  = {"pineapple","mango","papaya"}
thisisset.update(anotherset)
print(thisisset)