#Q41
'''
import sys 
alph = sys.argv[1]
mat = sys.argv[2]
mis = sys.argv[3]

print(' ', end='')
for nt in alph: 
	print(nt, end=' ')
print()


for i in range(0, len(alph)): 
	print(alph[i], end=' ')
	for j in range(0, len(alph)): 
		if i == j: print(mat, end =' ')
		else: print(mis, end=' ')
	print() 


for nt1 in alph: 
	print(nt1, end=' ')
	for nt2 in alph: 
		if nt1 == nt2: print(mat, end =' ')
		else: print(mis, end=' ')
	print() 
'''

#Q42 
'''
for a in range(1, 15): 
	for b in range(a+1, 15): 
		c = (a**2 + b**2)**0.5
		if c % 1 != 0: continue 
		print(a, b, c)
'''

#Q45
'''
def polya(dna): 
	longest = 0 
	for i in range(len(dna)): 
		if dna[i] == 'A': 
			for j in range(i, len(dna)): 
				if dna[j] != 'A': break 
			run = j - i 
			if run > longest: longest = run 
	return longest 

seq = 'AATCGAATCGAAAAAAGTC'
print(polya(seq))
'''

#Q46 char.count.py 
'''
import sys 
char = [0] *128 

with open(sys.argv[1]) as fp: 
	for s in fp: 
		for c in s: 
			char[ord(c)] +=1
for i in range(len(char)): 
	if char[i] == 0: continue
	if i <33: print(i, char[i])
	else: print(chr(i), char[i])
'''

#Q47 gc.analysis.py <fasta> <window>
'''
import sys 
seq = sys.argv[1]
w = int(sys.argv[2])

for i in range(len(seq)-w+1): 
	win = seq[i: i+w]
	g = win.count('G')
	c = win.count('C')
	gc_comp = g+c/w
	if g+c == 0: gc_skew = 0 
	else: gc_skew = (g-c)/(g+c)
	print(i, win, g, c, gc_comp, gc_skew)
'''

#Q48 function dust(seq, w, t)
'''
import math 
def entropy(seq): 
	pa = seq.count('A')/len(seq)
	pc = seq.count('C')/len(seq)
	pg = seq.count('G')/len(seq)
	pt = seq.count('T')/len(seq)
	h = 0 
	if pa != 0: h -= pa * math.log2(pa)
	if pc != 0: h -= pc * math.log2(pc)
	if pt != 0: h -= pt * math.log2(pt)
	if pg != 0: h -= pg * math.log2(pg)
	return h 
'''

'''
def dust(seq, w, t): 
	nseq = list(seq)
	for i in range(len(seq) +1-w): 
		win = seq[i:i+w]
		if entropy(win)<t: 
			for j in range(i, i+w): 
				nseq[j] = nseq[j].lower()
	return ''.join(nseq)

s = 'ATCGACTAAAAAAAAAAAAAAAGCTC'
print(dust(s, 8, 1 ))
'''
'''
w = 8
t = 1.0
seq = 'AGCGATCGAAAAAAAGCGCT'
nseq = list(seq)
for i in range(len(seq)-w+1): 
	if entropy(seq[i:i+w]) < t: 
		for j in range(i, i+w): 
			nseq[j] = 'N'
	print(''.join(nseq))
'''
















