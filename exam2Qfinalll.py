#Q21
def gc_comp(dna): 
	gc_count = 0 
	for base in dna: 
		if base == 'G' or base =='C': 
			gc_count += 1
	return gc_count/len(dna)

sequence = input('Enter DNASeq:')
print('GC composition:', gc_comp(sequence))

#Q22
import sys 

DNASeq = sys.argv[1]

def oligo_tm(dna): 
	A = dna.count('A')
	T = 
	C = 
	G = 
	length = A+T+C+G
	if length <= 13: 
		tm= 
	else: 
		tm = 
	return tm 


#Q23
import sys 
state = True

for words in sys.argv[1:]:
	for letters in words: 
		state = not state
		if state: 
			print(letter.upper(), end = '')
		else: 
			print(letter.lower(), end = '')
	print('', end = '')
print() 


#Q24
def anti(nt): 
	reverse_comp = ''
	for base in nt[::-1]: 
		if base == 'A': reverse_comp += 'T'
		elif T
		elif C
		elif G
	return reverse_comp
	

#Q25
import math 
import sys 

def entropy(P): 
	if not math.isclose(sum(P),1.0): sys.exit('not sum to one')
	H = 0 
	for p in P: 
		if p > 0: 
			H -= p * math.log2(p)
	return H 

#Q26
def maxstr(strings): 
	longest = strings[0]
	for s in strings[1:]: 
		if len(s) > longest: longest = s 
	return longest 


#28
def minmax(X): 
	mini = X[0]
	maxi = X[0]
	for i in X[1:]: 
		if mini > i: mini = i 
		if maxi < i: maxi = i 
	return mini, maxi 

#Q29 
def stats(X)
	n = len(X)

	mean = sum(X)/n 

	variance = 0 
	for x in X: 
		variance += (x-mean)**2
		variance = variance /n 
		std = variance ** 0.5


	sorted_X = sorted(X)
	if n % 2 ==1: 
		median = sorted_X[n//2]
	else: 
		mid1 = sorted_X[n//2]
		mid2 = sorted_X[n//2 -1]
		median = (mid1+mid2)/2

	return mean, std, median 


#Q31 
def pairwise_percent(s1, s2): 
	diff = 0 
	for c1, c2 in zip(s1, s2): 
		if c1 != c2: diff+=1
	return 1-diff/len(s1)

#Q33
import sys 
import math 

def dkl(P,Q): 
	if not math.isclose(sum(P), 1.0): sys.exit('error')
	if not math...
	distance = 0 
	for p, q in zip(P,Q): 
		if p == 0: continue 
		if q == 0: return float('inf')
		distance += p * math.log2(p/q)
	return distance 
	
	
	
#Q35 
def hydropathy(seq): 
	aas = 'ACDEFGHIKLMNPQRSTVWY'
	kdh = (1.8, 2.5, -3.5, -3.5, 2.8, -0.4, -3.2, 4.5, -3.9, 3.8, 1.9, -3.5, -1.6,
	-3.5, -4.5, -0.8, -0.7, 4.2, -0.9, -1.3)
	

	total = 0 
	
	for aa in seq: 
		idx = aas.index(aa)
		total += kdh[idx]
	return total /len(seq)


#Q37 
import random 
inside = 0 
outside = 0 

while True: 
	x = random.random()
	y = random.random() 
	if (x**2 + y**2) <=1: inside +=1
	else: outside +=1 
	print (4 * inside/(inside+outside))


#Q38 
import random
def random_dna(n, X=[])
	bases = [ATCG]
	sequence = random.choices(bases, weights = x, k = n)
	return ''.join(sequence)
	

#Q39 
import random 
	def random_subseq(seq, n, k)
	max_start = len(seq) - k 
	subsequnence = []
	for i in range (n): 
		start = random.randint(0, max_start)
		sub = seq[start: start_k]
		subsequence.append(sub)
	return subsequence 



max_start = len(seq)-k 
subsequence = []
for i in range(n): 
	start = random.randint(0, max_start)
	sub = seq[start: start +k]
	subsequence.append(sub)





#Q40 
import random 
	def mutate(dna, P): 
		bases = 'ATCG'
		mutated = []
		for i in dna: 
			if random.random() < p: 
				change = bases.replace(i, '') 
				mutated.append(change)
			else: 
				mutated.append(i)
		return ''.join(mutated)


bases = ''
mutated = []
	for i in dna: 
		if random.random() < p: 
			changes = bases.replace(i, '')
			mutated.append(changes)








