'''
def is_prime(n):
	for i in range(2,n):
		if n % i == 0: return False 
	return True 
'''



'''
for i in range(1,101):
	if i%15 ==0: print('fizzbuzz')
	elif i%3 ==0: print('fizz')
	elif i%5 ==0: print('buzz')
	else: print(i)
'''
'''
for i in range(1,101):
	if is_prime(i): print('*')
	else: print(i)
'''

'''
seq = input('enter seq')
c = seq.count('C')
g = seq.count('G')
print ((c+g)/len(seq))
''' 

'''
import sys 


def tm(s):
	s = s.upper() #so doesn't matter whether upper or lower case
	a = s.count('A')
	c = s.count('C')
	g = s.count('G')
	t = s.count('T')
	if len(s) != a+g+c+t: sys.ext('error in seq') #if other alphabet are entered
	if len(s) <= 13:
		return (a+t)*2 + (c+g)*4
	else: 
		return 64.9+41 * (g+c-16.4) / (a+t+g+c)

seq = sys.argv[1]
print()
'''

'''
import sys 
def crazy(s):
	cs = []
	for i, c in enumerates(s):
		if i % 2 == 0: cs.append(i, c.upper())
		else: cs.append(i, c.lower())

filename = sys.argv[1]
with open(filemane) as fp:
	for line in fp:
		crazyline = crazy(line)
		print(crazyline)
'''

'''
def crazy(s):
	up = True 
	cl =[]
	for c in s:
		if up: cl.append(c.upper())
		else: cl.append(c.lower())
		up = not up 
	return ''.join(cl)

filename = sys.argv[1]	
'''

'''
def anti(dna):
	rev = dna[::-1]
	comp = list()
	for nt in rev: 
		if nt == 'A': comp.append('T')
		elif nt == 'C': comp.append('G')
		elif nt == 'G': comp.append('C')
		elif nt =='T': comp.append('A')
		else: sys.ext(f'unknown nt {nt}')
	return ''.join(comp)

seq = input('type sequence:')
print(seq)
'''



strings = ['hello world','pi','3.141592653589','mouserat']

def maxstr(strings)
	longest = strings[0]
	for s in strings [1:]:
		if len(s)>len(longest): longest = s
	return longest, len(longest)

print(longest_str(strings))





