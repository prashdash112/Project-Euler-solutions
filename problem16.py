'''
POWER DIGIT SUM
2**15 = 32768 and the sum of its digits is 3 + 2 + 7 + 6 + 8 = 26.

What is the sum of the digits of the number 2**1000?
'''



def pow_dig_sum(base,exp):
	add=0
	a=(base**exp)
	
	while (a!=0):
		add=add+int(a%10)
		a=(a//10)
	
	return(add)

if __name__=="__main__":
	print(pow_dig_sum(2,1000))


