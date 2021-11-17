#!/usr/bin/python3
def uppercase(str):
	for i in range(len(str)):
		a = ord(str[i])
		b = ord(str[i]) - 32
		c = 0
		if ord(str[i]) >= 97 and ord(str[i]) <= 122:
			c = 1
		print("{:s}".format(chr(b)) if c == 1  else "{:s}".format(chr(a)),end='')
	print("\n")
