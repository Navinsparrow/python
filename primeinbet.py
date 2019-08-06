x, y = map(int,input().split())  
for au in range(x+1,y-1):  
   if au> 1:  
       for i in range(2,au):  
           if (au % i) == 0:  
               break  
       else:  
           print(au,end=(" "))  
