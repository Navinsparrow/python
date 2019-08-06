x,y= map(int,input("").split())
for nk in range(x+1,y):  
   sum = 0  
   temp = nk  
   while temp > 0:  
       digit = temp % 10  
       sum += digit ** 3  
       temp //= 10  
       if nk == sum:  
            print(nk,end=(" ")) 