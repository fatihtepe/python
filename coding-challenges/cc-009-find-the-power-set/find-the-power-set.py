def func (arr):
  power_set = []
  smalllist =[]
  for i in arr:
    smalllist = []
    smalllist.append(i)
    power_set.append(smalllist)
    
    for a in power_set:     
      tmp = a.copy()
      if i not in a:
        tmp.append(i)
        power_set.append(tmp)
  

  print(power_set)
