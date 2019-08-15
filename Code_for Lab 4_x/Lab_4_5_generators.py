foo = [1, 2, 3, 4, 5]

def my_enumerate(lst):   # Define own enumerate function
	for item in lst:     # Loop for generation objects with yield
		yield lst.index(item)+1, item  # Return tuple with 2 items - item index +1 and item value

		
for item in my_enumerate(foo):
	print(item)