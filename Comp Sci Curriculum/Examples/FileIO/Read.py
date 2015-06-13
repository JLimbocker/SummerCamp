
my_file = open("output.txt", "r")


for line in my_file:
	print line.rstrip()


my_file.close()