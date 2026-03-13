import sys 
import mcb185

'''
#calculate GC comp of each seq separately 

for defline, seq in mcb185.read_fasta(sys.argv[1]): 
	defwords = defline.split()
	name = defwords [0]
	gc = 0 
	for nt in seq: 
		if nt == 'C' or nt == 'G': 
			gc += 1 
	print(name, gc/len(seq))
'''


#to count 5 type of nucleotides for a.thaliana 

for defline, seq in mcb185.read_fasta(sys.argv[1]): 
	defwords = defline.split()
	name = defwords [0]
	A = 0 
	T = 0 
	C = 0 
	G = 0 
	N = 0 
	for nt in seq: 
		if nt == 'A': A+=1
		elif nt == 'C': C+=1
		elif nt == 'G': G += 1
		elif nt == 'T': T +=1
		else: 	N +=1 
	print(name, A/len(seq), C/len(seq), G/len(seq), T/len(seq), N/len(seq))


#used counts, but give same result 
for defline, seq in mcb185.read_fasta(sys.argv[1]): 
	defwords = defline.split()
	name = defwords [0]
	counts = [0,0,0,0,0]
	for nt in seq: 
		if nt == 'A': counts[0]+=1 
		elif nt =='C': counts[1] +=1
		elif nt =='G': counts[2] +=1
		elif nt =='T': counts[3] +=1
		else:	counts[4]+=1
	print(name, end='')
	for n in counts: print (n/len(seq), end = '')
	print()

#use string.find() to replace the if/elifs
for defline, seq in mcb185.read_fasta(sys.argv[1]): 
	defwords = defline.split()
	name = defwords [0]
	nts = 'ATCGN'
	counts = [0] * len(nts)
	for nt in seq: 
		idx = nts.find(nt)
		counts[idx] += 1 
	print(name, end='')
	for n in counts: print(n/len(seq), end='')
	




	
	
#to count ALL letter (not just ATCGN)
#used string.index() 
for defline, seq in mcb185.read_fasta(sys.argv[1]): 
	defwords = defline.split()
	name = defwords [0]
	nts = []
	counts = []
	for nt in seq: 
		if nt not in nts: 
			nts.append(nt)			#adding the new nt into list 
			counts.append(0)		#adding a position that starts at 0 in counts
		idx = nts.index(nt)
		counts[idx] += 1
	print(name)
for nt, n in zip(nts, counts): 
	print(nt, n, n/len(seq))
print() 



#use string.count() for specific letters within a sequence
for defline, seq in mcb185.read_fasta(sys.argv[1]): 
	defwords = defline.split()
	name = defwords [0]
	nts = []
	counts = []
	for nt in seq: 
		if nt not in nts: 
			nts.append(nt)
			counts.append(0)
		idx = nts.index(nt)
		counts[idx] += 1
	print(name, end='')
	for nt in 'ATCGN': 
		print(seq.count(nt) / len(seq), end='')
	print() 
















