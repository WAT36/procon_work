n,k=map(int,input().split())
r=sorted(list(map(int,input().split())))[n-k:]
ans=0
for i in range(len(r)):
    ans=(ans+r[i])/2
print(ans)