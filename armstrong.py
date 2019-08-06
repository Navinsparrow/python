x = int(input(""))  
sum = 0  
y = x 
  
while y > 0:  
   a = y % 10  
   sum += a ** 3  
   y //= 10  
  
if x == sum:  
   print("yes")  
else:  
   print("no") 