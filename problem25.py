import itertools


def fib_index():
	past = 1
	current = 0
	for i in itertools.count():
	
		if len(str(current)) == 1000:
			return str(i)
		
		past, current = current, past + current


print(fib_index())