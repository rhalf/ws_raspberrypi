#!/usr/bin/python3
languages = ["c++", "c#", "java", "php", "python"]         

# while iteration
print("while iteration")
it = iter(languages)
while True:
    try:
        print (next(it))
    except StopIteration:
        break

# for iteration
print("for iteration")
for language in languages:
    print(language)