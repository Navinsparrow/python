def recur_fibo(n):  
   if n <= 1:  
       return n  
   else:  
       return(recur_fibo(n-1) + recur_fibo(n-2))    
nterms = int(input())
if nterms > 0:  
   for i in range(0+1,nterms+1):  
       print(recur_fibo(i),end=" ")  