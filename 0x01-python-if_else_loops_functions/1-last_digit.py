#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
a = number % 10
if a < 0:
	print("Last digit of " + str(number) + "is " + str(a)
	+ " and is less than 6 and not 0")
elif a == 0:
	print("Last digit of " + str(number) + "is " + str(a)
	+ " and is 0")
else
	print("Last digit of " + str(number) + "is " + str(a)
	+ "and is greater than 5")
