#New 
import re

hand = open('somefile.txt')
for line in hand:
	line = line.rstrip()
	if re.search('^From:', line) :
		print(line)
		
