#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
a = abs(number) % 10
if number < 0:
	a = a * -1
if a < 0:
	print("Last digit of {:d} is {:d} and is less than 6 and not 0"
	.format(number, a))
elif a == 0:
	print("Last digit of {:d} is {:d} and is 0".format(number, a))
elif a > 5:
	print("Last digit of {:d} is {:d} and is greater than 5"
	.format(number, a))
else:
	print("Last digit of {:d} is {:d} and is less than 6 and not 0"
	.format(number, a))
