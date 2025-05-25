n,m=map(int,input().split())
v={}
for _ in range(m):
    a,b=map(int,input().split())
    v[a]=v.get(a, 0)+1
    v[b]=v.get(b, 0)+1

for ki,vi in v.items():
    if(vi%2!=0):
        print('NO')
        break
else:
    print('YES')
