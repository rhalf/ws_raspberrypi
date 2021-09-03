#!/usr/bin/python3
# sudo python3 activity17.py arg1 arg2
# import module sys
import sys

def main():
        for arg in sys.argv:
                print(arg)     
try:
        main()
except KeyboardInterrupt:
        pass
except Exception as exception:
        print(exception)
