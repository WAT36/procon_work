n,k=map(int,input().split())
ans=0

ans+=(6*(k-1)*(n-k))/(n**3)
ans+=(3*(n-k))/(n**3)
ans+=(3*(k-1))/(n**3)
ans+=1/(n**3)
print(ans)