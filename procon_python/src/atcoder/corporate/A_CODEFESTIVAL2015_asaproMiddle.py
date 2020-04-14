n,k,m,r=map(int,input().split())
s=[]
for _ in range(n-1):
    s.append(int(input()))

s.sort()

x=(k*r)-sum(s[max(n-k-1,0):])
if(x<=0):
    print(0)
else:
    x=(k*r)-sum(s[n-k:])
    if(x>m):
        print(-1)
    else:
        print(x)