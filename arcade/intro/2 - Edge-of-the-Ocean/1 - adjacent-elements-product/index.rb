def adjacentElementsProduct(inputArray)
    inputArray.each_cons(2).map { |a,b| a*b }.max
end