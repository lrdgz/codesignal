def nightRoute(city):
	res = []
	y = []
	count = 0
	for x in range(0, len(city)-1):
		# print city[x]
		_city = [ _x for _x in city[x] if _x >= 0]
		# print sum(_city)
		# if not min(_city):
		# 	y.append(min(_city))
		# 	if len(y) == 2:
		# 		# break
		# 		count += 1
		# 		y = []
		# else:
		# 	y = []
		res.append(min(_city))

	_x = []
	for x,y in enumerate(res):
		if not y:
			try:
				if res[x+1]:
					try:
						if not res[x+2]:
							_x.append(x+1)
					except:
						pass
			except:
				pass
			# print x
			# if res[x+1]:
				# if not res[x+2]:
					# _x.append(res[x+1])

		# print "%s ---- %s" % (x, y)

	for _y in _x:
		res[_y] = 0
	# print res

	# print count
	# print sum(res) - count
	# return sum(res) - count
	print(sum(res))
	return sum(res)
	


# nightRoute([[-1,5,20], [21,-1,10], [-1,1,-1]]) # Output 15
# nightRoute([[-1,3,2], [2,-1,0], [-1,0,-1]]) # Output 2
# nightRoute([[-1,2], [2,-1]]) # Output 2
nightRoute([[-1,-1,19,8,18,-1,-1,-1,-1,-1],  [10,6,4,7,0,10,18,-1,0,-1],  [-1,-1,15,-1,17,3,-1,14,16,3],  [4,19,3,15,8,4,6,11,5,8],  [5,3,10,-1,0,14,15,1,16,5],  [-1,8,-1,-1,5,-1,5,0,1,-1],  [-1,18,-1,19,2,-1,10,-1,8,6],  [14,8,12,16,-1,-1,0,16,15,17],  [4,5,1,12,0,4,8,15,1,-1],  [13,7,17,-1,4,13,16,3,12,9]]) # Output 14

# Consider a big city located on n islands. There are bridges connecting the islands, but they all have only one-way traffic. To make matters worse, most of the bridges are closed at night, so there is at most one bridge with traffic going from any island A to any other island B.

# There is a programmer who turns a penny by working nights as an Uber driver. One night his phone dies right after he picks up a rider going from island 0 to island (n - 1). He has the map of the city bridges in his laptop though (stored as a matrix of distances), so he decides to implement an algorithm that calculates the shortest path between those two islands and evaluate the cost based on the distance of the path. Assume that each mile of the trip is 1$.

# Example

# For

# city = [[-1, 5, 20],
#         [21, -1, 10],
#         [-1, 1, -1]]
# the output should be nightRoute(city) = 15.

# city[i][j] equals the distance between the ith and the jth islands in miles, or -1 if there is no bridge with traffic from island i to island j.

# nightRoute(city) should be 15, since the shortest distance from the 0th to the 2nd island is 15. The distance from the 0th to the 1st is city[0][1] = 5, and from the 1st to the 2nd is city[1][2] = 10.

# Input/Output

# [time limit] 4000ms (py)
# [input] array.array.integer city

# The city is represented as a square matrix, where city[i][j] equals the distance between the ith and the jth islands in miles, or -1 if there is no bridge with traffic in that direction.

# Constraints:
# 2 <= city.length <= 10,
# city[i].length = city.length,
# -1 <= city[i][j] <= 30.

# [output] integer

# The cost of the trip. It is guaranteed that there is a route from the 0th to the (n - 1)th island.


# [
# 	[-1, 5, 20], ==== 16
# 	[21, -1, 10], ==== 12 - 1
# 	[-1, 1, -1] ==== 3 - (-1)
#	=== 15
# ]