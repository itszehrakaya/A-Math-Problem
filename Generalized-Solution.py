def solution():
  a = input(int())
  b = input(int())
  c = input(int())
  multiples = [x for x in range(1,int(a)) if (x % (int(c))) == 0]
  total = [y for y in range(1,int(a)) if (y % (int(b)) == 0 and (y % (int(c))) != 0)]
  multiples.extend(total)
  print(sum(multiples))
 
solution()
