from collections import deque
n=int(input())
MOD=10007
a=[0,0,1]
l=3
if(n<=l):
    print(a[n-1]%MOD)
else:
    q=deque()
    q.append(0)
    q.append(0)
    q.append(1)
    for i in range(4,n+1):
        ai=sum(q)%MOD
        a.append(ai)
        q.popleft()
        q.append(ai)
    print(a[-1]%MOD)
