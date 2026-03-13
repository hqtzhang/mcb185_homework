import sys 

state = True 

for word in sys.argv[1:]:
	for letter in word: 
		state = not state
		if state: print(letter.upper(), end='')
		else: print(letter.lower(), end='')
	print(' ', end='')
print()