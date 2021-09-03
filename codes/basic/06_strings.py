#!/usr/bin/python3
# assignments
s1 = 'hi raspberry'
print(s1)
s2 = "hello python3"
print(s2)
s3 = """
    python
    rpi
"""
print(s3)
# accessing and substring
print(s1[0])                # h
print(s2[6:])               # python3
print(s1[0:2])              # hi
print(s1[0:2] + s2[6:])     # hi python3
print(s1[0:2] * 2)          # hihi
print("h" in s1)            # True
print("hi" in s1)           # True
print("z" in s1)            # False
print(s1.index("y"))        # 11
# length
print(len(s1))              # 12



