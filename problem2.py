"""Each new term in the Fibonacci sequence is generated by adding the previous two terms. By starting with 1 and 2, the first 10 terms 
will be:
1, 2, 3, 5, 8, 13, 21, 34, 55, 89, ...
By considering the terms in the Fibonacci sequence whose values do not exceed four million, find the sum of the even-valued terms."""

def fibo(n_terms):
	if n_terms==0:
		return(1)
	elif n_terms==1:
		return(2)
	else:
		return(fibo(n_terms-1) + fibo(n_terms-2))
#print(fibo(5))

# Driver function
def fibo_even(vals): # max size of a value 
	arr=[]
	i=0
	while fibo(i)<vals:
		i=i+1
		if(fibo(i)%2==0):
			arr.append(fibo(i))
	print(sum(arr))

fibo_even(4000000)

