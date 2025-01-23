'''
Python JSON

JSON is a  syntax for storing and exchanging data
JSON is text, written with Javascript object Notation

'''

'''
JSON in Python 


Parse JSON - convert from JSON to  Python 

json.loads()

'''


# json to python 
import json
x = '{"name" : "Ajay", "age":30, "city" : "Bangalore"}'

#parse x 
y = json.loads(x)

# the result is a  Python dictionary 

print(y["name"])



'''
Convert from Python to JSON

If  you have a   python object, you can convert it  into a  JSON string by using json.dumps() method 
'''

import json

x  = {

    "name" : "Ajay",
    "age" : 22,
    "city" : "Bangalore"

}


# convert  into JSON

print(json.dumps(x, indent=4))
