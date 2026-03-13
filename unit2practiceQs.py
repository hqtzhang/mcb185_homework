vals = [42313, 12, -243, 3.123]


def minimum(vals):
	mini = vals[0]
	for val in vals [1:]:
		if val < mini: mini=val
	return mini
print(minimum(vals))

def minmax(vals): 
	mini = vals[0]
	maxi = vals[0]
	for val in vals[1:]:
		if mini > val: mini = val
		if maxi < val: maxi = val
	return mini, maxi 
print(minmax(vals))

def mean(vals): 
	total = 0 
	for val in vals: total += val 
	return total / len(vals)
print(mean(vals))


