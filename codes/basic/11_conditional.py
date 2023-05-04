#!/usr/bin/python3
a, b = 1, 2
# if statement single line
if (True): print ("condition is true")
# if else statement
if (a == b) : print("a is equal to b")    
else : print("a is not equal to b")
# if elif else statement
if (a == b) : 
    print ("a is equal to b")    
elif (a > b) : 
    print ("a is greater than b")    
elif (a < b) : 
    print ("a is less than b")
else :
    print("default result")

#multiple condition
if (a == 1 or a == 2): print("a is equal to 1 or 2")
else: print("a must equal to 1 or 2")

if (a == 1 and a == 2): print("a is equal to 1 and 2")
else: print("a must equal to 1 and 2")