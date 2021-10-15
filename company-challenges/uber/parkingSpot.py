def parkingSpot(carDimensions, parkingLot, luckySpot):

	lengthCar, widthCar = carDimensions
	numRows = len(parkingLot)
	numCols = len(parkingLot[0])

	if isNotLuckySpotAvailable(parkingLot, luckySpot):
		return False
	
	widthSpaceInParkingLot = {'left':[],'top':[],'right':[],'bottom':[]}
	
	luckySpotSumFirst = luckySpot[2] - luckySpot[0] + 1
	luckySpotSumSecond = luckySpot[3] - luckySpot[1] + 1

	if luckySpotSumFirst == carDimensions[0] and luckySpotSumSecond == carDimensions[1]:
		widthSpaceInParkingLot = getVerticalSpaceAvailables(parkingLot, widthSpaceInParkingLot, numRows, numCols, widthCar, lengthCar)
	elif luckySpotSumFirst == carDimensions[1] and luckySpotSumSecond == carDimensions[0]:
		widthSpaceInParkingLot = getHorizontalSpaceAvailables(parkingLot, widthSpaceInParkingLot, numRows, numCols, widthCar, lengthCar)

	for key in widthSpaceInParkingLot:
		for spaces in widthSpaceInParkingLot[key]:
			if lengthCar <= spaces[2]:
				return True

	return False



def isNotLuckySpotAvailable(parkingLot, luckySpot):
	
	if sum(luckySpot[0:2]) < sum(luckySpot[2:4]):
		firstCoord = luckySpot[0:2]
		secondCoord = luckySpot[2:4]
	else:
		firstCoord = luckySpot[2:4]
		secondCoord = luckySpot[0:2]

	for x in range(firstCoord[0], secondCoord[0]+1):
		for y in range(firstCoord[1], secondCoord[1]+1):
			if parkingLot[x][y] == 1:
				return True
	return False




def getHorizontalSpaceAvailables(parkingLot, widthSpaceInParkingLot, numRows, numCols, widthCar, lengthCar): 


	if lengthCar > numCols:
		return widthSpaceInParkingLot

	horizontalMode = [['left',0], ['right', numCols - 1]]

	for h in horizontalMode:

		chekingSide, chekingRow = h

		for n in range(numRows):

			if parkingLot[n][chekingRow] == 0:

				if (numRows - n) >= widthCar:
					isAvailableSize = True

					for m in range(n, n+widthCar):

						if parkingLot[m][chekingRow] == 1:
							isAvailableSize = False
							break

					if isAvailableSize:

						widthSpaceInParkingLot[chekingSide].append([n,chekingRow,0])

		for i in range(len(widthSpaceInParkingLot[chekingSide])):
			x, y, size = widthSpaceInParkingLot[chekingSide][i]
			isAvailableSize = True
			sizeCount = 0


			for n in range(numCols):

				if isAvailableSize == False:
					break

				for w in range(widthCar):
					if chekingSide == 'left':
						freeSpace = parkingLot[x+w][y+n]
					elif chekingSide == 'right':
						freeSpace = parkingLot[x+w][y-n]

					if freeSpace == 1:
						isAvailableSize = False
						break

				if isAvailableSize:
					sizeCount += 1
					widthSpaceInParkingLot[chekingSide][i][2] = sizeCount
	return widthSpaceInParkingLot






def getVerticalSpaceAvailables(parkingLot, widthSpaceInParkingLot, numRows, numCols, widthCar, lengthCar): 

	if lengthCar > numRows:
		return widthSpaceInParkingLot

	verticalMode = [['top',0], ['bottom', numRows - 1]]

	for v in verticalMode:

		chekingSide, chekingCol = v
		for n in range(numCols):

			if parkingLot[chekingCol][n] == 0:
				if (numCols - n) >= widthCar:
					isAvailableSize = True

					for m in range(n, n+widthCar):

						if parkingLot[chekingCol][m] == 1:
							isAvailableSize = False
							break
					if isAvailableSize:
						widthSpaceInParkingLot[chekingSide].append([chekingCol,n,0])

		for i in range(len(widthSpaceInParkingLot[chekingSide])):
			x, y, size = widthSpaceInParkingLot[chekingSide][i]
			isAvailableSize = True
			sizeCount = 0

			for n in range(numRows):

				if isAvailableSize == False:
					break



				for w in range(widthCar):
					if chekingSide == 'top':
						freeSpace = parkingLot[x+n][y+w]
					elif chekingSide == 'bottom':
						freeSpace = parkingLot[x-n][y+w]

					if freeSpace == 1:
						isAvailableSize = False
						break
				if isAvailableSize:
					sizeCount += 1
					widthSpaceInParkingLot[chekingSide][i][2] = sizeCount
	return widthSpaceInParkingLot



# TEST = Originals test cases

print('# No. 1')
carDimensions = [3, 2]
parkingLot = [
    [1,0,1,0,1,0],
    [0,0,0,0,1,0],
    [0,0,0,0,0,1],
    [1,0,1,1,1,1]]
luckySpot = [1, 1, 2, 3]
print(parkingSpot(carDimensions, parkingLot, luckySpot))
print('true')
print('-------------------------------------------------------------------')
print('\n\n')


print('# No. 2')
carDimensions = [3, 2]
parkingLot = [
    [1,0,1,0,1,0],
    [1,0,0,0,1,0],
    [0,0,0,0,0,1],
    [1,0,0,0,1,1]]
luckySpot = [1, 1, 2, 3]
print(parkingSpot(carDimensions, parkingLot, luckySpot))
print('false')
print('-------------------------------------------------------------------')
print('\n\n')


print('# No. 3')
carDimensions = [4, 1]
parkingLot = [
    [1,0,1,0,1,0],
    [1,0,0,0,1,0],
    [0,0,0,0,0,1],
    [1,0,0,0,1,1]]
luckySpot = [0, 3, 3, 3]
print(parkingSpot(carDimensions, parkingLot, luckySpot))
print('true')
print('-------------------------------------------------------------------')
print('\n\n')


print('# No. 4')
carDimensions = [2, 1]
parkingLot = [
    [1,0,1],
    [1,0,1],
    [1,1,1]]
luckySpot = [0, 1, 1, 1]
print(parkingSpot(carDimensions, parkingLot, luckySpot))
print('true')
print('-------------------------------------------------------------------')
print('\n\n')


print('# No. 5')
carDimensions = [4, 2]
parkingLot = [
    [0,0,0,1],
    [0,0,0,0],
    [0,0,1,1]]
luckySpot = [0, 0, 1, 3]
print(parkingSpot(carDimensions, parkingLot, luckySpot))
print('false')
print('-------------------------------------------------------------------')
print('\n\n')


# print '# No. 6'
# carDimensions = [7, 2]
# parkingLot = [
# [0,1,0],
# [0,0,0],
# [0,0,0],
# [0,0,0],
# [0,0,0],
# [0,0,0],
# [0,0,0],
# [0,0,0]]
# luckySpot = [1, 0, 7, 1]
# print parkingSpot(carDimensions, parkingLot, luckySpot)
# print 'true'
# print '-------------------------------------------------------------------'
# print '\n\n'


# print '# No. 7'
# carDimensions = [5, 3]
# parkingLot = [
# [1,1,1,1,1,0,1,1,1,1],
# [0,1,0,0,1,0,0,0,0,0],
# [0,0,0,0,0,0,0,0,1,0],
# [0,0,0,0,0,0,0,0,0,0],
# [0,0,0,0,0,0,0,0,0,1],
# [0,0,0,0,0,0,0,0,1,0],
# [0,0,1,0,0,0,0,0,0,0],
# [1,0,0,0,0,0,0,0,0,0]]
# luckySpot = [1, 3, 5, 5]
# print parkingSpot(carDimensions, parkingLot, luckySpot)
# print 'false'
# print '-------------------------------------------------------------------'
# print '\n\n'


# print '# No. 8'
# carDimensions = [2, 1]
# parkingLot = [
# [1,0,1],
# [1,0,1],
# [1,1,1]]
# luckySpot = [1, 1, 2, 1]
# print parkingSpot(carDimensions, parkingLot, luckySpot)
# print 'false'
# print '-------------------------------------------------------------------'
# print '\n\n'


# print '# No. 9'
# carDimensions = [2, 1]
# parkingLot = [
# [1,1,1],
# [1,0,1],
# [1,0,1]]
# luckySpot = [0, 1, 1, 1]
# print parkingSpot(carDimensions, parkingLot, luckySpot)
# print 'false'
# print '-------------------------------------------------------------------'
# print '\n\n'


# print '# No. 10'
# carDimensions = [2, 1]
# parkingLot = [
# [1,1,1,1],
# [1,0,0,0],
# [1,0,1,0]]
# luckySpot = [2, 1, 2, 2]
# print parkingSpot(carDimensions, parkingLot, luckySpot)
# print 'false'
# print '-------------------------------------------------------------------'
# print '\n\n'


# print '# No. 11'
# carDimensions = [2, 1]
# parkingLot = [
# [1,1,1,1], 
# [1,0,0,0], 
# [1,0,1,0]]
# luckySpot = [1, 2, 1, 3]
# print parkingSpot(carDimensions, parkingLot, luckySpot)
# print 'true'
# print '-------------------------------------------------------------------'
# print '\n\n'


# print '# No. 12'
# carDimensions = [7, 2]
# parkingLot = [
# [0,0,0,0,0,0,0,0], 
# [1,0,0,0,0,0,0,0], 
# [0,0,0,0,0,0,0,0]]
# luckySpot = [1, 1, 2, 7]
# print parkingSpot(carDimensions, parkingLot, luckySpot)
# print 'true'
# print '-------------------------------------------------------------------'
# print '\n\n'