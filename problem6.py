# Problem 6 of project euler

arr=[]
arr1=[]
for item in range(1,101):
	arr.append(item)
	arr1.append(item**2)
	y=sum(arr)
	z=sum(arr1)
	y=y**2
print(y)
print(z)
print(y-z)