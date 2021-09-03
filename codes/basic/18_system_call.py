#!/usr/bin/python3

# import module subprocess
import subprocess

def main():
        command = ["cat", "/etc/os-release"]
        data = subprocess.call(command)
        print(data)
try:
        main()
except KeyboardInterrupt:
        pass
except Exception as exception:
        print(exception)


