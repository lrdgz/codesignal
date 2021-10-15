def perfectCity(departure, destination):
	import re

	x = departure
	y = destination
	res = 0


	if departure == destination:
		return 0

	
	for count in range(0, len(x)):
		# Do quick action if there are floats
		if(type(x[count]) == float):
			if(type(y[count]) == float):
				# If both float are equal
				if (x[count] == y[count]):
					# If the float did not rounded digit incremented by but become a whole number itself
					if(int(x[count] == round(x[count]))):
						# Then advance to the next point on the axis
						res += (int(x[count]) + 1) - x[count]
					else:
						# fall on the previous point of the axis
						res += x[count]
						x[count] += res
				# If the destination float is greater than the departure float
				elif (y[count] > x[count]):
					# This condition is used to know if the departure-axis is ahead by one or more points
					if (x[count] + 1) <= y[count]:
						# It just means we need to get to the point coordinate so we can just subtract the departure axis to the destination
						res += (int(x[count]) + 1) - x[count]
					else:
						# This is to determine if it is on the same point range
						if(int(x[count]) == int(y[count])):
							# Get the decimal number on the float to do conditionals
							_x = float(re.search(r"[.][\d]", str(x[count])).group())
							_y = float(re.search(r"[.][\d]", str(y[count])).group())
							# If the departure decimal subtracted to the a whole number is larger than the departure decimal then
							# then just go back to the previous point because it is nearer
							if (_x) <= (1-_y):
								# (0.2, 0.5) will be a 0.7 steps ==== [(0.2 - 0) + (0.5 - 0)]
								# The other way around will take us 1.3 steps ===== [(1 - 0.2) + (1 - 0.5) ]
								res = _x
								x[count] -= res
							# Otherwise advance to the next point because it will definitely be nearer	
							else:
								# (0.9, 0.4) will be a 0.7 steps ==== [(1 - 0.4) + (1 - 0.9) ]
								# The other way around will take us 1.3 steps ===== [(0.4 - 0) + (0.9 - 0)]
								res += (1 - _x)
								x[count] += res
								print(res)
								print(x)
				else:
					return 0


	res += abs(x[0] - y[0])
	res += abs(x[1] - y[1])
	print(res)
	# The technique is to get the fitted point coordinate to reach the destination like (0.4, 1) to (1.0, 1)
	# Turn every float coordinate into whole integer
	return res


perfectCity([0, 3], [0, 4]) # output 1
perfectCity([0.2, 0], [0.5, 7]) # output 7.7
perfectCity([0.2, 0], [1, 7]) # output 7.8
perfectCity([1, 0.4], [3, 0.9]) # output 2.7
perfectCity([0.4, 3], [0.4, 4]) # output 1.8
perfectCity([0.4, 1], [0.9, 3])  # output 2.7
perfectCity([3, 1], [5, 7.3]) # output 8.9
perfectCity([0, 0.2], [7, 0.5]) # output 7.7
perfectCity([0.9, 6], [1.1, 5]) # output 1.2
perfectCity([0, 0.4], [1, 0.6]) # output 2
perfectCity([1, 2.4], [7.3, 5]) # output 8.9



# https://codefights.com/fight/NJWGw4f9YAiT55Mct
# Consider a city where the streets are perfectly laid out to form an infinite square grid. In this city finding the shortest path between two given points (an origin and a destination) is much easier than in other more complex cities. As a new Uber developer, you are tasked to create an algorithm that does this calculation.

# Given user's departure and destination coordinates, each of them located on some street, find the length of the shortest route between them assuming that cars can only move along the streets.

# Example

# For departure = [0.4, 1] and destination = [0.9, 3], the output should be
# perfectCity(departure, destination) = 2.7.



# Input/Output

# [time limit] 4000ms (py)
# [input] array.float departure

# An array [x, y] of x and y coordinates. It is guaranteed that at least one coordinate is integer.

# Constraints:
# 0.0 <= departure[i] <= 10.0.

# [input] array.float destination

# The destination is given the same way as the departure location.

# Constraints:
# 0.0 <= destination[i] <= 10.0.

# [output] float

# The shorted distance between two points along the streets.