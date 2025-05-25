a,b,c,k=map(int,input().split())
ans=0

if(k<=a):
    ans+=k
    k=0
else:
    ans+=a
    k-=a

if(k<=b):
    k=0
else:
    k-=b

if(k>0):
    ans-=k
    k=0

print(ans)