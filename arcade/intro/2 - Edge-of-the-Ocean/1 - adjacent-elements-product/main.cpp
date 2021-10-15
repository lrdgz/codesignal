int adjacentElementsProduct(vector<int> inputArray) {
    int product=inputArray.at(0)*inputArray[1];
	for (int i=1;i<inputArray.size()-1;i++){
		int productTemp=inputArray.at(i)*inputArray[i+1];
		if(product<productTemp){
			product=productTemp;
		}

	}

	return product;
}
