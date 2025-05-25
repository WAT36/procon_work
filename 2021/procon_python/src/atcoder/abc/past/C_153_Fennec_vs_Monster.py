n,k=map(int,input().split())
h=list(map(int,input().split()))
h.sort()
h=list(reversed(h))
ans=0
for i in range(n):
    if(i>=k):
        ans+=h[i]
print(ans)