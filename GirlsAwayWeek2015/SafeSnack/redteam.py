# print "Hello World!"

known_fingerprints = [1, 2, 3, 4, 5, 6]

access_levels = [3, 1, 2, 1, 1, 3]

# print "the access level of id " + str(known_fingerprints[3]) + " is " + str(access_levels[3])






f_a_l = { 14:3, 2:1, 3:2, 4:2, 5:3, 6:1 }
f_a_l[14]


inventPrices = { "apple": [5, 0.50], "banana": [4, 0.75], "bread": [2, 2.50], "bean": [3, 0.99], "pasta": [4, 1.49]}


totalCost = 0
for key in inventPrices:
	quantity = inventPrices[key][0]
	cost = inventPrices[key][1]
	
	print "You have " + str(quantity) + " " + key + "s which cost $" + str(cost) + " each so that is a total cost of $" + str( quantity * cost )
	
	totalCost = totalCost + quantity*cost
	print totalCost
	
print "Your total cost is: $" + str( totalCost )
# print f_a_l[6]


print "Inventory:"

print 

inventory = { "apple": 5, "banana":4, "bread":2, "bean":3, "pasta":4}

# print "you have " + str(inventory["banana"]) + " bananas"

inventory["potato"] = 1

# print "you have " + str(inventory["potato"]) + " potatos"


food = raw_input("What food is that?")



print 

print "Adding one " + food

print 



if food in inventory:
	inventory[food] = inventory[food] + 1 
	
else: 
	inventory[food] = 1 
	 


for key in inventory:
	print "you have " + str(inventory[key]) + " " + key + "s"
