
# here we will go over the importance of whitespace in Python
# and the relevancy of variable scope


"""

draw a similar scope diagram


----
    var
    ----
    ----
    	----
    	----
    ----
----
----


"""

my_var = 5


if True:
	my_var = 10

	if my_var == 5:
		my_var = 15
	else:
		my_var = 20

print my_var