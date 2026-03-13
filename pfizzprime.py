#print 1:100
#if prim print fizz
#run program
#pipe it to grep, remove all nonfizz 
#redirect output to file fizz.txt 


def is_prime(n): 
	for i in range (2, n): 
		if n % i== 0: return False
	return True 
		

for i in range(1, 101): 
	if is_prime(i): print(i, 'fizz')
	else: print(i)
	
#| grep -v fizz > fizz.txt