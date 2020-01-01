import math
n=int(input())
while(True):
    rootn=math.sqrt(n)//1
    if(n == rootn**2):
        break
    else:
        n-=1
print(n)