import bisect
n,m=map(int,input().split())
x,y=map(int,input().split())
a=list(map(int,input().split()))
b=list(map(int,input().split()))
t=0
ans=0
while(True):
    ai=bisect.bisect_left(a, t)
    if(ai>=n):
        break
    t=a[ai]+x

    bi=bisect.bisect_left(b,t)
    if(bi>=m):
        break
    t=b[bi]+y
    ans+=1
print(ans)
