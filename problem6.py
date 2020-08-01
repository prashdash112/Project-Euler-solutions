'''
# Problem 6 of project euler
The sum of the squares of the first ten natural numbers is 385
The square of the sum of the first ten natural numbers is 3025
Hence the difference between the sum of the squares of the first ten natural numbers and the square of the sum is 2640

Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.

'''


arr=[]
arr1=[]
for item in range(1,101): # 100 natural nos
	arr.append(item)
	arr1.append(item**2)
	y=sum(arr)
	z=sum(arr1)
	y=y**2
print(y)
print(z)
print(y-z)
