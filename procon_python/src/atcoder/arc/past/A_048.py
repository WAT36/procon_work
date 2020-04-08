a,b=map(int,input().split())
ans=b-a
if(a*b<0):
    ans-=1
print(ans)