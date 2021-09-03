#!/usr/bin/python3
# single assignment
age = 3                  # An integer
name = "Juan"            # A string
isOk = False             # A Boolean
print (age, name, isOk)
# multiple assigment
a = b = c = 143
d, e, f = "hi", True, 0
print (a,b,c)
print (d,e,f)
# remove reference
del a
del b, c, d, e, f
print (a,b,c)
print (d,e,f)