'''
2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.

What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?

'''

import math

def lcm():
	a = 1
	for i in range(1, 21):
		a *= i // math.gcd(i, a)
	return str(a)


if __name__ == "__main__":
	print(lcm())
