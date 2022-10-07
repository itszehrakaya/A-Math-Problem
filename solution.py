
multiples = [ numbers for numbers in range(1,1000) if numbers % 3 == 0 ] # return numbers that are multiples of 3 below 1000.
total = [ numbers for numbers in range(1,1000) if (numbers % 5 == 0 and numbers % 3 != 0)] # return numbers that are multiples of 5 but not of 3 below 1000.
multiples.extend(total) 
sum(multiples)

