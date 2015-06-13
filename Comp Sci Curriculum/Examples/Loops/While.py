

"""

while [condition]:
	[contents]

LOOK OUT FOR INFINITE LOOPS
"""

import time

my_int = 1

while my_int < 11:
	print my_int
	my_int = my_int + 1

print "\n\n"


#count backwards

my_int = 5

while my_int > 0:
	print my_int
	my_int = my_int - 1
	time.sleep(1)

print "Boom!"