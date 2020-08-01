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
for i in range(int(15)):
    if is_prime(i)==True:
        p_no += 1
        arr.append(i)
print(arr)
print(arr[3])
print ("We found " + str(p_no) + " prime numbers.") 



