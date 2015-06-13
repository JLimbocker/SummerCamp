
"""
range([start], [stop], [step])

default step is 1

"""

print "count to 10: "
for i in range(1,11):
	print i

print "\n\n"



import time

# count backwards
for i in range(5,0,-1):
	print i
	time.sleep(1)

print "Boom!"
