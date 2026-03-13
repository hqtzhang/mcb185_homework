'''
import sys 

def read_fasta(filename): 
	seq = []
	with open(filename) as fp: 
		for line in fp: 
			seq.append(line.rstrip())
	seqline = ''.join(seq[1:])
	words = seq[0]
	uniqueid = words.split()[0][1:]
	return uniqueid, seqline

uniqueid, seqline = read_fasta(sys.argv[1])
'''

'''
import sys
import mcb185


for defline, seq in mcb185.read_fasta(sys.argv[1]): 
	print(defline, seq): 
	for frame in range(3): 
		pro = mcb185.translate(seq[frame:])
		print(defline, seq, pro)
'''

'''
import random

def random_word_set(n, k): 
	words = set()
		for i in range(n): 
			word = ''
			for j in range(k): 
				letter
				word += 
			words.add(words) 
		return words
'''	


#q49 dust.py
import math

def entropy(seq):
	pa = seq.count('A')/len(seq)
	pc = seq.count('C')/len(seq)
	pg = seq.count('G')/len(seq)
	pt = seq.count('T')/len(seq)
	h = 0 
	if pa != 0: h -= pa * math.log2(pa)
	if pc != 0: h -= pa * math.log2(pc)
	if pg != 0: h -= pa * math.log2(pg)
	if pt != 0: h -= pa * math.log2(pt)
	return h 

seq = 'AGCACGTCAAAAAAGCGCGCGTT'
w = 5
t = 1.5
mask = list(seq)
for i in range(len(seq) -w +1): 
	win = seq[i:i+w]
	h = entropy(win)
	if h <t: 
		for j in range (i,i+w): 
			mask[j] = 'N'
print(''.join(mask))













