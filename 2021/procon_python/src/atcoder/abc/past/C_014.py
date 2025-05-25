n=int(input())
qlen=1000002
maxb=0
q=[0 for i in range(qlen)]
for i in range(n):
    a,b=map(int,input().split())
    q[a] = q[a]+1
    q[b+1] = q[b+1]-1
    if(maxb < b+1):
        maxb = b+1
ans=0
nowval=0
for i in range(maxb):
    if(q[i] != 0):
        nowval+=q[i]
        if(ans < nowval):
            ans = nowval

print(ans)