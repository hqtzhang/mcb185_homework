import mcb185
import sys 

#in terminal, to import mcb185: 
#	cd ~/Code/mcb185_homework
#	ln -s ~/Code/MCB185/src/mcb185.py .

for defline, seq in mcb185.read_fasta(sys.argv[1]): 
	print(defline [:30], seq[:40], len(seq))