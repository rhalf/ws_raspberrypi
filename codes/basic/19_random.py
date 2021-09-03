#!/usr/bin/python3
#import module random
import random
def main():
        # random value between 0 - 1
        print(random.random())
        # create a list
        alp = [ "a","b","c","d","e"]
        print(alp)
        # get random item from list 
        print(random.choice(alp))
        # create another list
        nos = [ "1","2","3","4","5"]
        print(nos) 
        # shuffle the items from the list     
        random.shuffle(nos)   
        print(nos)     
try:
        main()
except KeyboardInterrupt:
        pass
except Exception as exception:
        print(exception)

