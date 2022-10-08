
multiples = [ x for x in range(1,1000) if x % 3 == 0 ] # return numbers that are multiples of 3 below 1000.
total = [ y for y in range(1,1000) if (y % 5 == 0 and y % 3 != 0)] # return numbers that are multiples of 5 but not of 3 below 1000.
multiples.extend(total) 
sum(multiples)

