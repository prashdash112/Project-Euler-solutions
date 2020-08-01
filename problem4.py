"""
# Program to check whether a no is palindrome or not
n=5005
temp=n
rev=0

while(n>0):
	dig=n%10
	rev=rev*10+dig
	n=(n//10)

if(rev==temp):
	print("palindrome")

else:
	print("Not palindrome")"""


# Solution to the problem 4 of project euler 
def comp():
	q=max(i*j 
		for i in range(100,1000) 
		for j in range(100,1000)
		if(str(i*j)==str(i*j)[: : -1]))
	return(q)

print(comp())
