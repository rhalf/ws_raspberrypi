#!/usr/bin/python3
# import the filename of the module w/o ext. name
import activity21 as person

def main():
        fname = person.getFirstName()
        print(fname)
        lname = person.getLastName()
        print(lname)
try:
        main()
except KeyboardInterrupt:
        pass
except Exception as exception:
        print(exception)


