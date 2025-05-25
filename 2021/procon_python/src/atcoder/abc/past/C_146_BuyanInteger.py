import math
a,b,x=map(int,input().split())

digits=0
i=0
while(True):
    n=10**i
    if(a*n + b*len(str(n)) > x):
        digits=i
        break
    i+=1

ans=(x - b*digits)//a
if(ans > 10**9):
    ans=10**9
else:
    while(a*(ans+1) + b*len(str(ans+1)) <= x):
        ans+=1
    while(ans>0 and a*ans + b*len(str(ans)) > x):
        ans-=1

print(ans)