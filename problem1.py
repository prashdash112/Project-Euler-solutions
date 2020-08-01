
"""If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.
Find the sum of all the multiples of 3 or 5 below 1000."""

def multipliers(muls):
	arr=[];
	for mul in range(1,muls+1):
		if((mul%3==0) or (mul%5==0)):
			arr.append(mul)
	print(sum(arr)) 

multipliers(999)


