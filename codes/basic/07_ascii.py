#!/usr/bin/python3
# American Standard Coded Information Interchange - ASCII
print("DEC\tBIN\tOCT\tHEX\tChar")
for index in range(255):
    print(
        str(index) + "\t" + 
        bin(index) + "\t" + 
        oct(index) + "\t" + 
        hex(index) + "\t" + 
        chr(index)
    )
# escape characters
#   back slash      description
#   \b              backspace
#   \s              space
#   \r              carriage return
#   \t              tab
#   \v              vertical tab
#   \n              newline
#   \e              escape