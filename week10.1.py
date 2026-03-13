'''
s = 'abcd'
for c1 in s: 
	for c2 in s: 
		print(c1, c2)

for i in range(0, len(s)): 
	for j in range(i+1, len(s)): 
		print(i, j, s[i], s[j])

import sys 
sys.exit()
'''







#Q42

import sys 
import random 

num_days = int(sys.argv[1])			#things coming off straight from sys is string, need to make it integer
num_people = int(sys.argv[2])
bdays = []


#find same bday by make a list of bdays of all ppl 
'''
found = False
for _ in range(num_people): 
	date = random.randint(0, num_days -1)			#ran.randint() upper bound include the bounded number 
	if date in bdays: 
		found = True
		break					#loop, not necessary, but imply it will break once it found same bdays
	bdays.append(date)
print(found)
'''


#for i/integer in range(number): 
#for item in container: 


#find same bday by first creating a "calendar"
'''
for i in range(num_people): 
	date = random.randint(0, num_days-1)
	bdays.append(date)
found = False	
for i in range(0, num_people): 
	for j in range(i+1, num_people): 			#i+1 gets rid of redundant, so only unique pairing. 
		if bdays[i] == bdays[j]: 
			found = True 
			break 								#to break the j loop 
	if found: break 							#to break the i loop 
print(found)			
'''


#make a calendar LIST

calendar = [0] * num_days

for i in range(num_people): 
	date = random.randint(0, num_days-1)
	calendar[date] += 1
print(calendar )

found = False 
for i in range(num_people): 
	if calendar [i] > 1: 
		found = True 
		break
print(found)


#bdays counts by checking the calendar as cal goes 
'''
calendar = [0] * num_days
found = False 
for i in range(num_people): 
	date = random.randint(0, num_days -1 )
	if calendar[date] == 0: 
		calendar[date] += 1 
	else: 
		found = True 
		break 
print(found)
'''


#Q41
'''
python3 print_matrix.py ACGT +1 -1
   A  C  G  T
A +1 -1 -1 -1
C -1 +1 -1 -1
G -1 -1 +1 -1
T -1 -1 -1 +1
'''

#header
'''
import sys 
alph =sys.argv[1]
mat = sys.argv[2]
mis = sys.argv[3]


print('  ', end =' ')			#for header: create the space before the ACGT
for nt in alph: 
	print(nt, end = '  ')		#for header: print the ACGT with space b/w
print() 						#for header: end the line 
'''

#for rest of matrix
'''
for nt1 in alph: 
	print(nt1, end = ' ')
	for nt2 in alph: 
		if nt1 == nt2: print(mat, end =' ')
		else: print(mis, end = ' ')
	print() 
'''


#for rest of matrix using loop
'''
for i in range(0, len(alph)):
	print(alph[i], end=' ')
	for j in range(0, len(alph)): 
		if i == j: print(mat, end=' ')
		else: print(mis, end=' ')
	print() 
'''







#Q49: write a function dust(seq, w,t)

import math 
def entropy(seq): 
	pa = seq.count('A') / len(seq)
	pc = seq.count('C') / len(seq)
	pg = seq.count('G') / len(seq)
	pt = seq.count('T') / len(seq)
	h = 0 
	if pa !=0: h -= pa * math.log2(pa)
	if pc !=0: h -= pc * math.log2(pc)
	if pg !=0: h -= pg * math.log2(pg)
	if pt !=0: h -= pt * math.log2(pt)
	return h
def dust(seq, w, t): 
	eseq = list(seq)
	for i in range(len(seq) -w+1): 
		win = seq[i:i+w]
		if entropy(win) < t: 
			for j in range(i, i+w): 
				eseq[j] = eseq[j].lower()			#to lower case
				#eseq[j] = 'N'
	return ''.join(eseq)			#join the list to string

print(dust('ACGTAAAAAAACGT', 6, 1.1))




#Q48 
'''
import sys 
seq = sys.argv[1]
k = int(sys.argv[2])
for i in range(len(seq) - k+1): 
	win = seq[i:i+k]
	g = win.count('G')
	c = win.count('C')
	gc_comp = (c+g)/k
	if g+c == 0: gc_skew = 0					#avoid error when in an window with no G/C
	else: 		 gc_skew = (g-c)/(g+c)
	print(i, win, c, g, gc_comp, gc_skew)
'''



#actual effective way to write it (no need), so we dont count the whole thing over and over again 
'''
first = seq[0:k]
g = first.count('G')
c = first.count('C')
for i in range(len(seq) -k +1): 
	off seq[i]
	on seq[i+k]
	if off == 'C': c-=1
	elif off == 'G': g-=1
	
	if on == 'C': c+=1
	elif on == 'G':  g +=1 	
	print(c, g)
'''












