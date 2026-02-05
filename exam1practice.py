#Q18
#fib starts with 0
# 1 1 2 3 5 8 13 21

a=0
b=0
fib = a+b 

while True: 
	a=b
	b=fib
	fib = a+b  
	if fib>100: break 
 	print(fib)

