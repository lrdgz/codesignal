def adjacentElementsProduct(inputArray):
    list = []
    for i in range(1, len(inputArray)):
        multip = inputArray[i -1]*inputArray[i]
        list.append(multip)
    
    return max(list)