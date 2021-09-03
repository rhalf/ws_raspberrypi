#!/usr/bin/python3
# an empty list
drinks = []
print(drinks)
# a list with items
drinks = ["tea", "coffee", 14344, "choco", False]
print(drinks)
# accessing          
print(drinks[0])            # "tea"
print(drinks[0][1])         # 'e'
print(drinks[0:2])          # ["tea", "coffee"]
print(drinks[3:])           # ["choco", False]
# adding
drinks.append("cafe macchiato")
print(drinks)
# updating
drinks[5] = "macchiato"
print(drinks)
# deleting item on list
del drinks[5]
print(drinks)
print(drinks + drinks)
# deleting the whole list
del drinks