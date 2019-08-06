import math
a,n,d=map(int,input().split())

total = (a * (2 * n + (a - 1) * d)) / 2
print(math.floor(total))
