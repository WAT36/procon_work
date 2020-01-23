n,k=map(int,input().split())
ans=1
for i in range(n):
    ans*=k
    if(i==0):
        k-=1
print(ans)