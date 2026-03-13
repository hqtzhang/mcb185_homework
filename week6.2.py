import sys 
import random 

people = int(sys.argv[1])
calendar = int(sys.argv[2])
iterations = int(sys.argv[3])

classroom = [1]
for i in range (people): 
	birthday = random.randint(0, calendar-1)
	classroom.append(birthday)
	
for b1 in classroom: 
	for b2 in classroom: 
		print (b1, b2) 

'''
#a half matrix to compare everyones bday, without comparing i with i
# if replace i+1 with just i, then compare include i with i 
# if we want the full matric without diagnol(selfcompare), then both i and j start with 0, 
# and add below for j in range: if i == j: continue

classroom = ['A', 'B', 'C', 'D']
for i in range(0, len(classroom)): 
	for j in range (i+1, len(classroom)): 
		print (classroom[i], classroom[j]) 
'''

'''
if classroom[i] == classroom[j] ==: print('same birthday')
'''



'''
#final version for solution 1 by listing in matrix 

import sys 
import random 

iterations = int(sys.argv[3])
people = int(sys.argv[1])
calendar = int(sys.argv[2])

sames = 0 
for_ in range (iterations): 
	classroom = []
	same_birthday = False 
	for i in range (people): 
	birthday = random.randint(0, calendar-1)
	if birthday in classroom: 
		same_birthday = True 
		break 
	classroom.append(birthday)
	
	same_birthday = False
	for i in range (o, len(classroom)): 
		for j in range(i+1, len(classroom)): 
			if classroom[i] == classroom[j]: 
				same_birthday == True
				break 

if same-birthday: sames += 1 

print (same/iterations)
'''

'''
# soulution2 by using a calendar 

import sys 
import random 


people = int(sys.argv[1])
day = int(sys.argv[2])
iterations = int(sys.argv[3])

same = 0 
for _ in range(iterations): 
	calendar = [0] * days 
	doe _ in range(people): 
		bday = random.randint(0, days-1)
		ifcalendar[bday] ==1: 
			same_birthday = True
			break 
		calendar[bday] +=1 
	
	same_birthday = False	
	for v in calendar: 
		if v > 1: 
			same-birthday = True 
			break 
	
	if same_birthday: sames += 1 

print(sames/iterations) 
'''


genome_size = int(sys.argv[1])
coverage = int(sys.argv[2])

genome = [0] * genome_size

for i in range (genome size * )






'''
#to solve for mean/median/max/min

vals.sort()

total = 0 
for val in vals: total += val
mean = total/ len(vals)

#median 
m = len(vals)//2
if len(vals) % 2 ==1: 
	median = vals[[m]    #when odd
else: 
	median = (vals[m] + vals[m-1])/2
	
	

print('min: ', vals[0])
print('max: ', vals[-1])
print('range: ', vals[-1] - vals[0]) 
print('average: ', mean)


'''



