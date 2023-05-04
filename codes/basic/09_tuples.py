#!/usr/bin/python3
# an empty tuples
languages = ()
print(languages)
# a tuples with items
languages = ("python", "java", "c++", "c#")
# accessing         
print(languages[0])         # python
print(languages[0:2])       # [python, java]
print(languages[3:])        # c#
print(languages[0][0])      # p

del languages