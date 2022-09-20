
multiples = [x for x in range(1,1000) if x%3 == 0]
total = [y for y in range(1,1000) if (y % 5 == 0 and y %3 != 0)]
multiples.extend(total)
sum(multiples)
