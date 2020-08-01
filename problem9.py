'''
A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,

a**2 + b**2 = c**2

There exists exactly one Pythagorean triplet for which a + b + c = 1000.
Find the product abc.

'''
'''
def pyth_trip(a,b,c):   # Alternate function to check the condition described in question 
	if (a**2+b**2)==c**2:
		if (a+b+c)==1000:
			return (a*b*c)
	else:
		False


print(pyth_trip(3,4,5))'''


import math
def pythagorean_triplet(n):  # No of digits
  for b in range(n):
    for a in range(1,b):
        c = math.sqrt( a * a + b * b)
        if c % 1 == 0:
        	if (a+b+int(c)==1000):
        		print(a*b*c)
        		print(a,b,c)


if __name__=="__main__":
	pythagorean_triplet(1000)


