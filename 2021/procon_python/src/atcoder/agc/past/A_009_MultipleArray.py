n=int(input())
a=[]
b=[]
for i in range(n):
    ai,bi=map(int,input().split())
    a.append(ai)
    b.append(bi)
ans=0
for i in reversed(range(n)):
    ai=a[i]+ans
    push=0 if ai%b[i]==0 else b[i]-(ai%b[i])
    ans+=push
print(ans)