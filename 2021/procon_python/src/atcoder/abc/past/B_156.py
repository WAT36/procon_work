n,k=map(int,input().split())
ans=0
while(n//(k**ans)>0):
    ans+=1
print(ans)