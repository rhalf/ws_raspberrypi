#!/usr/bin/python3
# import module time
import time
def main():
        a = time.time()
        # struct date and time
        print(time.localtime())
        # struct time
        print(time.localtime(a))
        # fomatted time
        print(time.asctime(
                time.localtime(a)))
        # delay
        for count in range(10):
                print(count)
                time.sleep(1)
try:
        main()
except KeyboardInterrupt:
        pass
except Exception as exception:
        print(exception)