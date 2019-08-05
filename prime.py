n=int(input(""))
flag = True
if n > 1:
  for i in range(2,n):
    if(n % i) == 0:
      print("no")
      flag = False
      break
  if(flag == True):  
    print("yes")
else:
  print("no")