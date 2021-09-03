#!/usr/bin/python3
a, b, c = 1, 5, 9
print("========arithmetic========")
print(a + b + c)    	# add 15
print(a - b - c)    	# sub -13
print(a * b * c)    	# mul 45
print(c / b)        	# div 1.8

print(c // b)       	# flr 1
print(c % b)        	# mod 4
print(b ** c)       	# exp 1953125
print("========comparison=======")
print(a == b)       	# is equal? False
print(a != b)       	# is not equal? True
print(a < b)        	# is less than? True
print(a > b)        	# is greater than? False 
print(a <= b)       	# is less than or equal? True 
print(a >= b)       	# is greater than or equal? False

#a = 0b00000001 or 0b1  
#b = 0b00000101 or 0b101
#c = 0b00001001 or 0b1001
print("=========bitwise========");
print(bin(a | b)) 	#bin or: 0b101
print(bin(a & b)) 	#bin and: 0b1
print(bin(a ^ b)) 	#bin xor: 0b100
print(bin(~a))    	#bin comp: -0b10
print(bin(a << 1))	#bin left shift: 0b10
print(bin(a >> 1))    	#bin right shift: 0b0

print("=========logical========")
print(True or False)	#c=|| ? True		
print(True and False)	#c=&& ? False
print(not True)		#c=! ? False