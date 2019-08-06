nk = int(input(""))  
factorial = 1  
if nk == 0:  
   print("1")  
else:  
   for i in range(1,nk + 1):  
       factorial = factorial*i  
   print(factorial)  