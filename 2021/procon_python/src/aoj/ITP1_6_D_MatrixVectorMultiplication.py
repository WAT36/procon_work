n,m=map(int,input().split())
a=[]
b=[]
for i in range(n):
    an=list(map(int,input().split()))
    a.append(an)

for j in range(m):
    b.append(int(input()))

ans=[]
for i in range(n):
    ai=a[i]
    ansi=0
    for j in range(m):
        ansi+=ai[j]*b[j]
    ans.append(ansi)

for i in range(len(ans)):
    print(ans[i])
