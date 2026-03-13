'''
#Q21
def gc_comp(dna):
	dna = dna.upper()
	gc_count = 0 
	for base in dna: 
		if base =='G' or base =='C': 
			gc_count += 1
	return gc_count/len(dna)

seq = input('Enter your DNA seq:')
gc = gc_comp(seq)
print("GC comp:",gc)

//


def gc_comp(dna): 
	gc_count = 0 
	for base in dna: 
		if base =='G' or base =='C': 
			gc_count += 1
	return gc_count/len(dna)

seq = input('Enter DNA seq:')
print('GC comp:', gc_comp(seq))
'''

'''
#Q22

import sys 

def oligo_tm(dna): 
	dna = dna.upper()
	
	A = dna.count('A')
	T = dna.count('T')
	C = dna.count('C')
	G = dna.count('G')
	
	len = A+T+C+G
	
	if len <=13: 
		tm = ((A+T) * 2 + (G+C) * 4)
	else: tm = 64.9 + 41 * (G+C -16.4) / (A+T+G+C)
	return tm 

putdna = sys.argv[1]

print(oligo_tm(putdna))
'''








'''
#Q24
def anti(nt):
    comp = {'A':'T', 'T':'A', 'C':'G', 'G':'C'}

    revcomp = ''
    for base in nt[::-1]:
        revcomp += comp[base]

    return revcomp

seq = 'AGCTACACG'
print(anti(seq))


def anti(nt): 
	nt = nt.upper()
	revcomp =''
	
	for base in nt[::-1]: 
		if base == 'A': 
			revcomp += 'T'
		elif base == 'T':
			 revcomp += 'A'
		elif base == 'C': 
			revcomp += 'G'
		elif base == 'G':
			 revcomp += 'C'
	return revcomp
	
seq = 'AGCTACACG'
print(anti(seq))
'''



'''
#Q25 
import math 
import sys 

def entropy(P): 
	if not math.isclose(sum(P), 1.0): 
		sys.exit('not sum to one')
	
	H = 0 
	for p in P: 
		if p > 0: 
			H -= p * math.log2(p)
	return H 

print(entropy([0.2, 0.3, 0.4]))
'''

'''
#Q26
def maxstr(strings): 
	if not strings: 
		return None 
	
	longest = strings[0]
	
	for s in strings [1:]:
		if len(s) > len(longest): 
			longest = s 
	
	return longest 

string1 = ('sadafea', 'fdadsd','sdfsadfsafg')

print(maxstr(string1))
'''

'''
#Q27
 
def minstrlen(strings): 
	if not strings: 
		return None
	
	shortest = len(strings[0])
	
	for s in strings [1:]:
		if len(s) < shortest: 
			shortest = len(s)
		return shortest

string2 = ('eq','dafew')

print(minstrlen(string2))
'''


'''
#Q28 
def minmax(X): 
	mini = X[0]
	maxi = X[0]
	for x in X[1:]:
		if x < mini: mini = x 
		if x > maxi: maxi = x
	return mini, maxi 

list1 = (12,23432,43423,-1323,1.2342)
print(minmax(list1))

#Q29 
def mean(X): 
	total = 0 
	for x in X: total += x 
	return total/len(X) 

print(mean(list1))





def stats(X): 
	n = len(X)

#mean
	mean = sum(X)/n
	
#sd
	variance = 0 
	for x in X: 
		variance += (x-mean) **2
	variance = variance/n 
	sd = variance ** 0.05

#median
	sorted_X = sorted(X)
	
	if n%2 == 1: 
		median = sorted_X[n // 2]
	else: 
		mid1 = sorted_X[n//2 -1]
		mid2 = sorted_x[n//2]
		median = (mid1 + mid2)/2
		
	return mean, sd, median 
		

print(stats(list1))
'''












