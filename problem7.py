'''
By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.

What is the 10 001st prime number?



'''



p_no = 0

def is_prime(x):
    if x >= 2:
        for y in range(2,x):
            if  not( x % y ):  #reverse the modulo operation
                return False
    else:
        return False
    
    return True
	        

arr=[]
for i in range(int(100000)):
    if is_prime(i)==True:
        p_no += 1
        arr.append(i)
print(arr)
print ("We found " + str(p_no) + " prime numbers.") 



