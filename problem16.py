def pow_dig_sum(base,exp):
	add=0
	a=(base**exp)
	
	while (a!=0):
		add=add+int(a%10)
		a=(a//10)
	
	return(add)

print(pow_dig_sum(2,1000))


