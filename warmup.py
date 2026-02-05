import math 

def is_prob(x):
	return 0 <= x <= 1

OR: 
if x<=0 return False
if x>=1 return False 
return True 


print(is_prob(0.5))


def distance(x1, y1, x2, y2):
	c = math.sqrt((x2-x1)**2 + (y2-y1)**2)
	return c 

OR:
return((x1-x2)**2 + (y1-y2)**2)**0.5

print (distance(1,2,3,4))


