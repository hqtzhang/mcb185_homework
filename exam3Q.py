#Q45 
'''
def polya(dna):
	longest = 0 
	for i in range(len(dna)): 
		if dna[i] == 'A': 
			for j in range(i, len(dna)): 
				if dna[j] != 'A': break 
			run = j-i
			if run > longest: longest = run 
	return longest

seq = 'AAGCAGGCTTAAAAG'
print(polya(seq))
'''


#Q42
'''
for a in range(1, 10):
    for b in range(a+1, 10):
        c = (a**2 + b**2) ** 0.5
        if c % 1 != 0: continue
        print(a, b, c)
'''









#Q46
'''
s = 'watasrr dfedew dd'
charac = []
char_count = []

for c in s: 
	if c not in charac: 
		charac.append(c) 
		char_count.append(1)
	else: 
		idx = charac.index(c)
		char_count[idx] += 1 
for c, n in zip(charac, char_count): 
	if ord(c) <= 32: print(ord(c), n)
	else: 			  print(c, n)

'''

import sys 
chars = [0] *128
with open(sys.argv[1]) as fp: 
	for s in fp: 
		for c in s: 
			chars[ord(c)] += 1 
for i in range(len(chars)): 
	if chars[i] == 0: continue 
	if i < 33: print(i, chars[i])
	else: print(chr(i), chars[i])






