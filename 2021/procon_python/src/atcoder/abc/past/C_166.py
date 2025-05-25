n,m=map(int,input().split())
g=[[] for i in range(n)]
h=list(map(int,input().split()))
used=set([])
for i in range(m):
    a,b=map(int,input().split())
    g[a-1].append(b-1)
    g[b-1].append(a-1)

ans=[]
for i in range(n):
    if(i in used):
        continue
    else:
        gi=g[i]
        hi=h[i]
        for j in gi:
            if(hi <= h[j]):
                break
        else:
            ans.append(i)
        used.add(i)
print(len(ans))