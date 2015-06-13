
"""
We will combine some skills we've already learned and make a
program that will ask you a question and give you a response
based on your answer.
"""

# give test_var an arbitrary value not equal to 'y' or 'n'
test_var = "0"

while test_var != "y" and test_var != "n":
	test_var = raw_input("Do you like coding? (y/n)")
	test_var = test_var.lower()

	if test_var != "y" and test_var != "n":
		print "Please enter \'y\' or \'n\'"



if test_var == "y":
	print "Of course you do! It\'s the best!"
else:
	print "You\'re a liar! Coding rocks!"