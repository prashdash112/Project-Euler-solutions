'''
n! means n × (n − 1) × ... × 3 × 2 × 1

For example, 10! = 10 × 9 × ... × 3 × 2 × 1 = 3628800,
and the sum of the digits in the number 10! is 3 + 6 + 2 + 8 + 8 + 0 + 0 = 27.

Find the sum of the digits in the number 100!

'''


def fact_sum(n): # function to find factorial of a no
	add=0
	if n==1:
		return 1
	else:
		y=n*fact_sum(n-1)
		return y


y=fact_sum(100) # instance of fact_sum

add=0
while y>0:
	add=add+int(y%10)
	y=y//10
print(add) # returns the sum of digits of 100!(factorial)


