year = int (input(""))

if((year%400 ==0)or(year%4 ==0)&(year%100!=0)):
  print("yes")
else:
  print("no")  