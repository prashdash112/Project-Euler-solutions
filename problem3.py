"""arr=[]
def lpf(no): 
	
	for i in range(1,no+1):
		if(no%i == 0):
			arr.append(i)
	return(arr)

print(lpf(845))

for item in arr:
	for n in range(1,item):
		if item%n==0:

print(item)
"""

# Python program to print prime factors
import math
# prime
def primeFactors(n):
   # no of even divisibility
   while n % 2 == 0:
      print (2),
      n = n / 2
   # n reduces to become odd
   for i in range(3,int(math.sqrt(n))+1,2):
      # while i divides n
      while n % i== 0:
         print (i)
         n = n / i
   # if n is a prime
   if n > 2:
      print (n)
n = 600851475143
primeFactors(n)

