import copy
h,w=map(int,input().split())
c=[]
for _ in range(10):
    c.append(list(map(int,input().split())))

a=[]
for _ in range(h):
    a.append(list(map(int,input().split())))


d=copy.copy(c)

for k in range(10):
    for i in range(10):
        for j in range(10):
            d[i][j] = min(d[i][j],d[i][k]+d[k][j])

ans=0

for hi in range(h):
    for ahi in a[hi]:
        if(ahi != -1):
            ans+=d[ahi][1]
print(ans)