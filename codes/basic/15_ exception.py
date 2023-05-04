#!/usr/bin/python3
def main():
       raise Exception("I am the only exception!")
try:
        main()
except KeyboardInterrupt:
        pass
except Exception as exception:
        print(exception)