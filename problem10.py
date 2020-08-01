'''
The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.

Find the sum of all the primes below two million.
'''



'''
p_no = 0                   #trivial method

def is_prime(x):
    if x >= 2:
        for y in range(2,x):
            if  not( x % y ):  #reverse the modulo operation
                return False
    else:
        return False
    
    return True
	        

arr=[]
for i in range(int(2000000)): # 2 million
    if is_prime(i)==True:
        p_no += 1
        arr.append(i)
print(arr)
print(sum(arr)) # sum of primes below 2 million 
print ("We found " + str(p_no) + " prime numbers.") 

'''

import eulerlib


# Call the sieve of Eratosthenes and sum the primes found.
def compute():
    ans = eulerlib.primes(1999999)
    ans=sum(ans)
    return str(ans)


if __name__ == "__main__":
    print(compute())

