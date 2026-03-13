'''
#Q30 color match
import sys 

filename = sys.argv[1]
target_r = int(sys.argv[2])
target_g = int(sys.argv[3])
target_b = int(sys.argv[4])

min_distance = 1000
min_color = None 

with open(filename) as fp: 
	for line in fp: 
		colorname, hexavalue, rgbs = line.split()
		r,g,b = rgbs.split(',')
		distance = 0 
		distance += abs(target_r - int(r))
		distance += abs(target_g - int(g))
		distance += abs(target_b - int(b))
		
		if distance < min_distance: 
			min_disntance = distance
			min_color = colorname 
		
print(min_color, min_distance) 



#OH revised

import sys 

filename = sys.argv[1]
target_r = int(sys.argv[2])
target_g = int(sys.argv[3])
target_b = int(sys.argv[4])

min_distance = 1000
min_color = None 

with open(filename) as fp: 
	for line in fp: 
		colorname, hexavalues, rgbs = line.split()
		r, g, b = rgbs.split(',')
		d2 = abs(target_r - int(r)) + abs(target_g - int(g)) + abs(target_b - int(b))
		dc = ((target_r - int(r))**2 + (target_g - int(g))**2 + (target_b - int(b))**2)**0.5
		if d2 < min_distance: 
			min_distance = d2 
			min_color = colorname 
		print(d2, dc)
print(min_color, min_distance)
'''



'''
#Q30 finalversion

import sys 

filename = sys.argv[1]
target_r = int(sys.argv[2])
target_g = int(sys.argv[3])
target_b = int(sys.argv[4])

min_distance = 1000
min_color = None 

with open(filename) as fp: 
	for line in fp: 
		colorname, hexavalues, rgbs = line.split()
		r, g, b = rgbs.split(',')
		d = ((target_r - int(r))**2 + (target_g - int(g))**2 + (target_b - int(b))**2)**0.5
		if d < min_distance: 
			min_distance = d 
			min_color = colorname 
print(min_color, min_distance)
'''


'''
#Q31
seq1 = 'AGCTACACT'
seq2 = 'AGCGGTAGG'

def pairwise_percent(s1, s2): 
	diff = 0 
	for n1, n2 in zip(s1, s2): 
		if n1 != n2: diff +=1 
	return 1 - diff/len(s1)

print(pairwise_percent(seq1, seq2))
'''

'''
#Q32
def manhattan(X1, X2): 
	d = 0 
	for x1, x2 in zip(X1, X2): 
		d += abs(x1-x2)
	return d 
	
P1 = [0.2, 0.4]
P2 = [0.5, 0.8]

print(manhattan(P1, P2))
'''


'''
#Q33
import math 
import sys

def dkl(P,Q): 
	if not math.isclose(1.0, sum(P)): sys.exit('error')
	if not math.isclose(1.0, sum(Q)): sys.exit('error')
	distance = 0
	for p, q in zip(P,Q): 
		if p == 0: continue
		if q == 0: return float('inf')
		distance += p * math.log2(p/q)
	return distance 

a = [0.5, 0.5]
b = [0.2, 0.8]

print(dkl(a,b))
'''












'''
#jaccard

import sys
file1 = sys.argv[1]
file2 = sys.argv[2]

def get_list_from_file(filename): 
	string = []
	with open(filename) as fp: 
		for line in fp: 
			string.append(line.rstrip())
		return string

def jaccard(f1, f2):
	X1 = get_list_from_file(f1)
	X2 = get_list_from_file(f2)
	unique_a = []
	unique_b = []
	shared = []
	for x1 in X1: 
		if x1 in X2: shared.append(x1)
		else: 		 unique_a.append(x1)
	for x2 in X2:
		if x2 not in X1: unique_b.append(x2)
	print(unique_a)
	print(unique_b)
	print(shared)
	return len(shared) / (len(unique_a) + len(unique_b) + len(shared)) 


print(jaccard(file1, file2))
'''





#Q35 Kyte doolittle scale

def hydropathy(seq): 
	aas = 'ACDEFGHIKLMNPQRSTVWY'
	kdh = (1.8, 2.5, -3.5, -3.5, 2.8, -0.4, -3.2, 4.5, -3.9, 3.8, 1.9, -3.5, -1.6,
	-3.5, -4.5, -0.8, -0.7, 4.2, -0.9, -1.3)
	
	total = 0 
	for aa in seq: 
		idk = aas.index(aa)
		total += kdh[idk]
	return total/len(seq)



print(hydropathy('AGW'))





'''
#Q36
import itertools

def translate(dna): 
	codons = [''.join(t) for t in itertools.product('ACGT', repeat=3)]
	trans = 'KNKNTTTTRSRSIIMIQHQHPPPPRRRRLLLLEDEDAAAAGGGGVVVV*Y*YSSSS*CWCLFLF'
'''




'''
#Q37.finite

#not infinte 
import random

inside = 0
outside = 0

for i in range(1000): 
	x = random.random()
	y = random.random()
	d = (x**2 + y**2) **0.05
	if d >1: outside += 1
	else: 	 inside += 1 
	print(4 * inside / (inside + outside))
'''

'''
#Q37.infinite
#to run infinite

import random

inside = 0 
outside = 0 

while True: 
	x = random.random()
	y = random.random()
	if (x**2 + y**2) <= 1: inside +=1
	else: outside +=1
	print (4*inside/(inside+outside))
'''



#Q38Correct
import random 

def random_dna(n, x = [0.25, 0.25, 0.25, 0.25]): 
	base = ['A', 'T', 'C', 'G']
	seq = random.choices(base, weights = x, k=n)
	return ''.join(seq)


print("Uniform: ", random_dna(130))



'''
#Q38 
import random

def random_dna(min_len, max_len, X=[0.25, 0.25, 0.25, 0.25]):
	bases = ['A', 'T', 'C', 'G']
	n = random.randint(min_len, max_len)
	seq = random.choices(bases, weights = X, k=n)
	return "".join(seq)



print(random_dna(100, 500, X=[0.1, 0.4, 0.4, 0.1]))
'''


#Q39 
import random 
def random_subseq(seq, n, k): 
	max_start = len(seq) - k
	subsequence = []
	for base in range(n): 
		start = random.randint (0, max_start)
		sub = seq[start : start + k]
		subsequence.append(sub)
	return subsequence 

dna_master = "ATGCGATCGTAGCTAGCTAGCTAGCTGATCGATCGATCG"
result = random_subseq(dna_master, n=3, k=5)

print(f"Master Sequence: {dna_master}")
print(f"Random Samples:  {result}")


import random 
def random_subseq（seq, n, k):
	max_start = len(seq) - k 
	subsequence = []
	for base in range (n): 
		start = random.randint(0, max_start)
		sub = seq[start : start + k]
		subsequence.append(sub)
	return subsequence 



'''
#Q40 


import random 

def mutate(dna, p): 
	base = 'ATCG'
	mutated = []
	for i in dna: 
		if random.random() < p: 
			change = base.replace(i , '')
			mutated.append(random.choice(change))
		else: 
			mutated.append(i)
	return ''.join(mutated)
			
original_dna = "GGGCCTAAATTGCC"
mutated_dna = mutate(original_dna, 0.5)
print(f"Original: {original_dna}")
print(f"Mutated:  {mutated_dna}")
'''
			
			
			
			
			


