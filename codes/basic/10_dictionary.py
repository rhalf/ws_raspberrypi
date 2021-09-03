#!/usr/bin/python3
# an empty dictionary
person = {}
print(person)
# a dictionary
person = { 
    "name" : "juan", 
    "age" : 21, 
    "height" : 5.6 
}
print(person)
# accessing          
print(person["name"])   #juan
print(person["age"])    #21
# adding 
person["weight"] = 74
print(person)
# updating dictionary
person["height"] = 5.7
print(person)
# deleting
del person["age"]
print(person)
# delete dictionary
del person