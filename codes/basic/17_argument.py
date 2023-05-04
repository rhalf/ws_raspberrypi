#!/usr/bin/python3
# sudo python3 lesson14.py p1 p2 p3
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
