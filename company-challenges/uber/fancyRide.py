def fancyRide(l, fares):
	freePromo = 20 # Free promo given by Uber is 20$
	# Cars from the most least to most expensive
	cars = ["UberX", "UberXL", "UberPlus", "UberBlack", "UberSUV"]
	carCount = len(fares)
	for x in range(0, carCount):
		cost = fares[x] * l
		if(cost > freePromo):
			print(cars[x-1])
			return cars[x-1]
	print(cars[carCount-1])
	return cars[carCount-1]

# fancyRide(30, [0.3, 0.5, 0.7, 1, 1.3])
fancyRide(15, [0.3, 0.5, 0.7, 1, 1.3])

# Being a new Uber user, you have $20 off your first ride. You want to make the most out of it and drive in the fanciest car you can afford, without spending any out-of-pocket money. There are 5 options, from the least to the most expensive: "UberX", "UberXL", "UberPlus", "UberBlack" and "UberSUV".

# You know the length l of your ride in miles and how much one mile costs for each car. Find the best car you can afford.

# Example

# For l = 30 and fares = [0.3, 0.5, 0.7, 1, 1.3], the output should be
# fancyRide(l, fares) = "UberXL".

# The cost for the ride in this car would be $15, which you can afford, but "UberPlus" would cost $21, which is too much for you.

# Input/Output

# [time limit] 4000ms (py)
# [input] integer l

# A positive number representing the length of the ride.

# Constraints:
# 4 <= l <= 30.

# [input] array.float fares

# A strictly increasing array of 5 elements. fares[0] stands for dollars per mile in "UberX", fares[1] is the same for "UberXL", etc.

# Constraints:
# 0.3 <= fares[i] <= 5.0.

# [output] string

# The car that you should choose: "UberX", "UberXL", "UberPlus", "UberBlack" or "UberSUV". It is guaranteed that you can afford at least one of them.