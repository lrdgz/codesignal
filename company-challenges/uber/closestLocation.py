def closestLocation(address, objects, names):
	# import re
	from math import sqrt
	
	start = [0, 0] # The starting point, this is where the uber driver will come from
	dists = [] # This where all the distances computed will be stored
	_names = [] # This is where all the invalid location names will be stored

	def nameAcceptance(name):
		# _address = r'%s' % address
		# x = re.match(_address, name, re.IGNORECASE) # Note that the comparison should be case-insensitive
		# if not x:
		y = name.split(" ")
		if len(y) > 0:
			for _y in y:
				# user's input has one extra symbol
				# user's input has one missing symbol
				diff =   len(_y) - len(address)
				# print diff
				if abs(diff) < 2:
					count = 0
					# Loop that parses the index and its value to compare the missing, extra and different symbol
					for index,symbol in enumerate(_y):
						if not diff: # user's input has different symbol
							if symbol.upper() != address[index].upper():
								count += 1
						elif(diff == 1): # user's input has missing symbol
							try: # This catch is used for cases where the extra symbol is on the leading edge like Cat'e' 
								if symbol.upper() != address[index-count].upper():
									count += 1
							except:
								pass
						else: # user's input has missing symbol
							if symbol.upper() != address[index+count].upper():
								count += 1
					if count < 2:
						return 1
		return 0

	# Loop to store all the invalid names
	for x in names:
		if not nameAcceptance(x): # Conditional to know if the names are valid
			_names.append(x) # If invalied store it to the _names array

	# Conditional to know if all names are invalid, so all will not be deleted leaving an empty array and just compare their distances
	if len(_names) != len(names):
		for x in _names:
			index = names.index(x)
			del names[index]
			del objects[index]

	# If only one name remains then return it immediately
	if len(names) == 1:
		print(names[0])
		return names[0]

	# Use Pythagorean Theorem if both coordinates has value because travel by diagonal is possible
	def coordinateValue(x, y):
		if x and y:
			res = sqrt(x**2 + y**2) # pythagorean theorem used if the coordinate is not on the edge like (2, 1).. **2 is squaring an integer 
		else:
			res = x + y # Equation used if the coordinate is on the edge or corner like (0, 1)

		# print res
		return res

	# START, logic of choosing if many names are similar
	for x in objects:
		_z = []
		# Conditional ued to know if it is a range of coordinates
		if len(x) > 2:
			# Variables created for easier and smoother looping
			_x = sorted([y  for y in x if x.count(y) == 1])
			_y = list(set([y  for y in x if x.count(y) > 1]))[0]
			# print _x
			# print _y
			# Loop to know all the axis parallel from the range of coordinates
			for z in range(_x[0], _x[1]):
				val = coordinateValue(abs(z), abs(_y))
				_z.append(val)
				# print [abs(z), abs(_y)]
			# print _z
			dists.append(min(_z))
		# Determines if it is a simple coordinate
		else:
			# print x
			_list = [ abs(_x) for _x in x ] # Makes everyting into positive for smooth calculation
			val = coordinateValue(_list[0], _list[1])
			dists.append(val)

	print(dists)
	res = dists.index(min(dists)) # Determines the closes location
	print(names[res])
	return names[res]
	# END, logic of choosing if many names are similar


# Output: "Cat avenue"
# [2, 2.23606797749979, 2.23606797749979, 1]
closestLocation(
	"Cat",
	[
		[-2,0], 
		[1,2], 
		[2,1,2,4], 
		[-3,-1,4,-1]
 	],
 	[
 		"Bat building", 
		"Cast exhibition", 
		"At street", 
		"Cat avenue"
 	]
)

# Output: "At street"
[3, 3.1622776601683795, 2.23606797749979, 3]	
closestLocation(
	"Cat",
	[
		[-3,0], 
		[1,3], 
		[2,1,2,4], 
		[-4,-3,6,-3]
 	],
 	[
 		"Bat building", 
		"Cast exhibition", 
		"At street", 
		"Cat avenue"
 	]
)

# Output: "Bat building"
[3, 3.1622776601683795, 2.23606797749979, 3]	
closestLocation(
	"Cat",
	[
		[-3,0], 
		[1,3], 
		[2,1,2,4], 
		[-4,-3,6,-3]
 	],
 	[
 		"Bat building", 
		"Cast exhibition", 
		"Ate street", 
		"Cat avenue"
 	]
)

# Output: "cAt street"
[3, 3.1622776601683795, 2.23606797749979, 3]	
closestLocation(
	"Cat",
	[
		[-3,0], 
		[1,3], 
		[2,1,2,4], 
		[-4,-3,6,-3]
 	],
 	[
 		"Bat building", 
		"Cast exhibition", 
		"cAt street", 
		"Cat avenue"
 	]
)

# Output: "Bat building"
[3, 3.1622776601683795, 2.23606797749979, 3]	
closestLocation(
	"Cat",
	[
		[-3,0], 
		[1,3], 
		[2,1,2,4], 
		[-4,-3,6,-3]
 	],
 	[
 		"Bat building", 
		"cat exhibition", 
		"ACATA ", 
		"Cat avenue"
 	]
)

# Output: "Bat building"
[3, 3.1622776601683795, 3]
closestLocation(
	"Cat",
	[
		[-3,0], 
		[1,3], 
		[2,1,2,4], # This is not indexed at search
		[-4,-3,6,-3]
 	],
 	[
 		"Bat building", 
		"Cast exhibition", 
		"Cramp", 
		"cat avenue"
 	]
)

# Output: "lcationaaaa"
[5, 4.242640687119285]
closestLocation(
	"Location",
	[
		[5,-10,5,10],
		[3,3]
 	],
 	[
 		"loocationnnn", 
		"lcationaaaa", 
 	]
)

# Output: "Location"
[2, 6]
closestLocation(
	"Location",
	[
		[1,1],
		[3,3]
 	],
 	[
 		"Locati", # This is not indexed at search
		"Location", 
 	]
)

# Output: "location2"
[100, 4.242640687119285]
closestLocation(
	"Location",
	[
		[100,0,200,0],
		[3,3]
 	],
 	[
 		"location1", 
		"location2", 
 	]
)

# Output: "est dfe"
[2.23606797749979, 2.23606797749979]
closestLocation(
	"test",
	[
		[2,1,2,4],
		[-1,2]
 	],
 	[
 		"est dfe", 
		"trest mmm", 
 	]
)

# Output: "uiz aaa"
[2.23606797749979, 2.23606797749979]
closestLocation(
	"quiz",
	[
		[2,1,2,4],
		[-1,2]
 	],
 	[
 		"uiz aaa", 
		"fuiz bb", 
 	]
)

# Output: "lcationaaaa"
[100, 4.242640687119285]
closestLocation(
	"Location",
	[
		[100,-1,100,1],
		[3,3]
 	],
 	[
 		"loocationnnn", 
		"lcationaaaa", 
 	]
)




# The Uber app has an integrated map that simplifies selecting a destination. To make it even better, Uber guesses the location even if there is a typo in the inputted address.

# Consider a map with streets and buildings located on the Cartesian plane with integer coordinates. The distances on this map are calculated as follows:

# The distance between two points is the length of the segment connecting them.
# The distance between a segment and a point is defined as the shortest distance between the given point and any point on the segment.
# A user has started to type in their destination, and it's your task to guess what they are looking for.

# Let the rider's position be at [0, 0]. Given the positions of some objects around them, and the address they have already typed in, find out what their destination is. To do this, find the object closest to the rider with a name that has a prefix which is similar to the text that's already entered. Since it's possible that there is a typo in the input, let similar mean one of the following:

# the typed in address is identical to the prefix of the object's address;
# they differ only by one symbol;
# user's input has one extra symbol;
# user's input has one missing symbol.
# Note that the comparison should be case-insensitive.

# For example, if the user typed in "Cat", the following can be suggested: "Cat street", "Bat building", "_At avenue" (the first letter is deleted), and "Cast exhibition".

# Example

# For address = "Cat", objects = [[-2, 0], [1, 2], [2, 1, 2, 4], [-3, -1, 4, -1]] and
# names = ["Bat building", "Cast exhibition", "At street", "Cat avenue"], the output should be
# closestLocation(address, objects, names) = "Cat avenue".

# Since all the names are similar to what the user has typed, and the distances to them are respectively 2, sqrt(5), sqrt(5) and 1 (see the picture below for better understanding).



# Input/Output

# [time limit] 4000ms (py)
# [input] string address

# The partial address the user has typed already.

# Constraints:
# 2 <= address.length <= 8.

# [input] array.array.integer objects

# objects[i] corresponds to the ith object. There are two type of objects:

# a building, which is represented as an array of two elements with x and y coordinates;
# a street, which is represented as an array of four elements with x and y coordinates at its start, and x and y coordinates at its end.
# It is guaranteed that each street is parallel to one of the axes.

# Constraints:
# 2 <= objects.length <= 8,
# -200 <= objects[i][j] <= 200.

# [input] array.string names

# The ith element is the name of the ith object.

# Constraints:
# names.length = objects.length,
# 2 <= names[i].length <= 15.

# [output] string

# Return the name of the object the user supposedly chose as their destination. It should be the name of the closest object that is similar to the typed text. If there are several such objects, return the one that appears first in the provided list.

# It is guaranteed that at least one object's name is similar to the typed text.