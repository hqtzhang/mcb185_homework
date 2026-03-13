'''
#Q42
for a in range (1, 15): 
	for b in range (a+1,15): 		#a+1 to avoid duplicate like 10 and 10
		c = (a**2 + b**2) ** 0.5
		if c % 1 != 0: continue 	#continue can skip the ones we dont want and move on
		print(a, b, c)
		
		

stuff = ('A', 'B', 'C', 'D')
for i in range(len(stuff)): 
	for j in range(i+1, len(stuff)): 
		print(stuff[i], stuff[j])
'''	
		
		
'''	
#Q43
import sys 
import random
cal = int(sys.argv[1])		#days in a year
ppl = int(sys.argv[2])		#number of ppl


shared = False 					#to allow only print out when we DO have same bday
bdays = [] 						#or you can do bdays=list(), basically people's bday in a list
for _ in range(ppl): 
	bdays.append(random.randint(0, cal-1)) 		#adding ppl's bday on the list
for i in range(ppl): 
	for j in range (i+1, ppl):
		if bdays[i] == bdays[j]: 
			shared = True 
if shared: print('yay')
else:      print('nope')
'''


'''
#Q44
import sys 
import random
cal = int(sys.argv[1])
ppl = int(sys.argv[2])

calendar = [0] * cal	#there's cal number of positions (for a year cal=365) that start with 0.
for _ in range(ppl): 
		date = random.randint(0, cal-1)
		calendar[date] += 1

shared = False						#to allow only print out when we DO have same bday
for date in range(cal): 
	if calendar[date] > 1: shared = True 
if shared: print('yay')
else: 	   print('nope')
'''

'''
#Q46

s = 'faede dfkewfpe dd'
characters = []
char_count = []
for c in s: 
	if c not in characters: 
		characters.append(c) 
		char_count.append(1)
	else: 
		idx = characters.index(c)
		char_count[idx] += 1 
for c, n in zip(characters, char_count): 
	if ord(c) <= 32: print(ord(c), n )
	else: 		     print(c, n)



# an alternative way of doing it by using ascii 
chars = [0] * 128 
for c in s: 
	chars[ord(c)] += 1 
for i in range(len(chars)): 
	if chars[1] == 0: continue 
	print(ascii(i), chars[i])
'''


#Q49 

seq = 'AGCGATCGAAAAAAAGCGCT'
hard ='AGCGATCGNNNNNNNGCGCT'
soft ='AGCGATCGaaaaaaaGCGCT'


import math 

def entropy(seq): 
	pa = seq.count('A')/len(seq)
	pc = seq.count('C')/len(seq)
	pg = seq.count('G')/len(seq)
	pt = seq.count('T')/len(seq)
	h = 0 
	if pa != 0: h -= pa * math.log2(pa)
	if pc != 0: h -= pc * math.log2(pc)
	if pg != 0: h -= pc * math.log2(pg)
	if pt != 0: h -= pc * math.log2(pt)
	return h
	
k = 5 	#window size
t = 1.0 #entropy threshold
mask = list(seq)

for i in range(len(seq) -k+1): 		#-k+1 to make sure the window goes to the very end
	if entropy(seq[i:i+k]) > t: continue 	#scan if each nucleotide(i) is lower than the threshold
	for j in range(i, i+k): 
		mask[j] = 'N'			#replace all A into N
		#use:  mask[j]= seq[j].lower()   to make it lower case
print(''.join(mask))



















































