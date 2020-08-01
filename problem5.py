import math

def lcm():
	a = 1
	for i in range(1, 21):
		a *= i // math.gcd(i, a)
	return str(a)


if __name__ == "__main__":
	print(lcm())