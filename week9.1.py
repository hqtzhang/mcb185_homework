#Q45

seq = 'AAAGCGTTAGCTGCAAAAAAAGGTC'

#for i, nt in enumerate(seq): 
#	if nt =='A':print(i,nt)

'''
max_run = 0 
for i in range(len(seq)): 
	if seq[i] == 'A': 
		run_start = i 
		run_len = 1 
		for j in range(i+1, len(seq)): 
			if seq[j] == 'A': run_len += 1 
			else: break
		if run_len > max_run: max_run = run_len 
print(run_start, max_run)
'''

'''
i = 0 
max_run = 0 
while i  < len(seq): 
	if seq[i] == 'A': 
		run_start = i 
		run_len = 1 
		for j in range(i+1, len(seq)): 
			if seq[j] == 'A': run_len += 1 
			else: break
		i = j 
		if run_len > max_run: max_run = run_len
	i += 1 
print(run_start, max_run)
'''


#Q49 dust, entropy filter 
'''
seq = 'ABCDEGFGH'
k = 4
for i in range(len(seq) -k+1): 
	win = seq[i: i+k]
	print(i, win)
'''

import math 

def entropy(s): 
	pa = s.count('A') / len(s)
	pc = s.count('C') / len(s)
	pg = s.count('G') / len(s)
	pt = s.count('T') / len(s)
	if pa != 0: pa = s.count('A') / len(s)
	if pc != 0: pc = s.count('C') / len(s)
	if pg != 0: pg = s.count('G') / len(s)
	if pt != 0: pt = s.count('T') / len(s)
	h = 0 
	h -= pa * math.log2(pa)
	h -= pc * math.log2(pc)
	h -= pg * math.log2(pg)
	h -= pt * math.log2(pt)
	return h 



#in program	
seq = 'AGCTAAAAAAAATGCA'
mask = 'AGCTNNNNNNNNTGCA'
sed = list(seq)

k = 4
for i in range(len(seq) -k+1): 
	win = seq[i: i+k]
	if entropy(win) < 1.0: 
		for j in range (i, i+k): 
			sed[j] == 'N'
print(''.join(sed))


#in function 
def dust(seq, k, t): 
	sed = list(seq)
	for i in range (len(seq) -k+1): 
		if entropy(seq[i: i+k]) < 1.0: 
			for j in range (i, i+k): 
				sed[j] == 'N'
	return ''.join(sed)
