def centuryFromYear(year)
    if (year % 100) == 0
      year / 100
    else
      (year - (year%100))/100 + 1
    end
end
  
# centuryFromYear(1705) => 18
# centuryFromYear(1900) => 19
# centuryFromYear(1601) => 17
# centuryFromYear(2000) => 20