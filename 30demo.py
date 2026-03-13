fp = open()
for line in fp: 
	do_smth_with(line)
fp.close()

import gzip 
with gzip.open(path, 'rt') as fp: 
	for line in fp: 
		print(line, end='')