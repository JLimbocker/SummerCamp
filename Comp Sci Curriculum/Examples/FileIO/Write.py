

my_file = open("output.txt", "w")


my_list = [2,3,4,5,6,7,8,9,10]



for item in my_list:
	my_file.write( str(item ** 2) + "\n")

my_file.close()