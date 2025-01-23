'''
File Hnadling :

the key function working  with files in python is  the open() function

the open() function  takes two parameters : filename  and mode

there are four methods (modes) for opening a file

File Handling in  Python allows  you to work with file  to read,write , append or even manipulate data stored in them, it is
essential for tasks like data processing, logging  , and  saving application stats 
'''

'''
"r" = Read 
"a" = append
"w" = write
"x" = create

"t" -  text 
"b" - Binary Mode
 '''


    
'''
File Operations

opening a  file

-> The  open() functiomn is  used to  open a  file , it returns a  file object 



'''

file = open("example.txt","r")
file.close()

'''
wit statement  to automatically close the file
'''

with open("example.txt","r") as file:
    content =  file.read()


'''
Reading Files

'''    

with open("example.txt", 'r') as  file:
    content = file.read()
    print(content)


with open("example.txt", "r") as file:
    for line in file:
        print(line.strip())    


# reading specific BYtes

with open("example.txt", "r") as file:
    content =  file.read(5)
    print(content)

#writing  files    

with  open("example.txt","w") as  file:
    file.write(" Hi This is a new words")



with open("example.txt", "r") as  file:
    content =  file.read()
    print(content)

lines = ["Line 1\n", "Line 2\n", "Line 3\n"]
with open("example.txt", "w") as file:
    file.writelines(lines)


# Appending to files

with open("example.txt", "a") as  file:
    file.write("\n this is an additional line ")


with open("example.txt", "r") as  file:
    content  =  file.read()
    print(content)


import os

if os.path.exists("exsssample.txt"):
    print("File Exists")
else:
    print("File Does not exist")    


from pathlib import Path

file = Path("exsssample.txt")
if file.is_file():
    print("file exists")



# exception handling  

try:
    with open("nonexistfile.txt", "r") as  file:
        content = file.read()
except FileNotFoundError:
    print("The file does not exist")        



if os.path.exists("example.txt"):
    os.remove("example.txt")
    print("  removed")
else:
    print(" The  file does not exist ")    
