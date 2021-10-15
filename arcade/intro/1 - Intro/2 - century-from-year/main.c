int centuryFromYear(int year) 
{
	int result = 0;
	result = year/100;
	if((year % 100) > 0)
	{
		result += 1;
	}
  	return result ;
}