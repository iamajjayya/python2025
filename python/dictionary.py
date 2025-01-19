'''
Python Dicitionaries

* Dictionaries are used to stote data values in key:value pairs
* A dictionary is a collection which is ordered*, changable,  and do  not allow duplicates

'''

thisdict  = {

    "brand":"Ford",
    "model":"Mustang",
    "year" :1964

}

print(thisdict["model"])
x =  thisdict.get("year")
print(x)
print(thisdict.keys())
print(thisdict["year"])
thisdict["color"] = "red"
print(thisdict)
thisdict.popitem()
print(thisdict)
thisdict.pop("brand")
print(thisdict)


for x , y in thisdict.items():
    print(y , x )



myfamily  = {
    "child1" : {
        "name":"Emil",
        "year":2004
    },
    "child2" : {
        "name":"Tobias",
        "year":2011
    }
}    

print(myfamily["child1"]["name"])


for x, obj in myfamily.items():
    print(x)

    for y in obj:
        print(y+ ":", obj[y])