



# the function must be defined before it is called
def my_function():
	print "We have a function!"


# here we are calling our function
my_function()



# functions can have parameters
def greet(name):
	print "Hello " + name

# call greet function with "Travis" as the parameter
greet("Travis")





# functions can return values
def square_number(number):
	return number ** 2

# call our function and print the value
print "The number squared is: " + str(square_number(4))

# we can assign return values to variables
my_value = square_number(28)
print my_value