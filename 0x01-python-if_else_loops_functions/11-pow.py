#!/usr/bin/python3
def pow(a, b):
	a1 = a
	c = 1
	if b > 0:
		for i in range(b - 1):
			a *= a1
	elif a > 0 and b < 0:
		for i in range(abs(b) - 1):
			a *= a
		a = 1 / a
	elif a < 0 and b < 0:
		a = abs(a)
		for i in range(abs(b) - 1):
			a *= a
		a = -1 / a
	else:
		a = 1
	return a
