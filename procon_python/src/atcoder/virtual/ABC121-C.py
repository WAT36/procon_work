n,m=map(int,input().split())

ab=[]
for i in range(n):
    ab.append(list(map(int,input().split())))
ab.sort(key=lambda x:x[0])

ans=0
now_b=0
for i in range(n):
    if(ab[i][1]+now_b<m):
        ans+=ab[i][0]*ab[i][1]
        now_b+=ab[i][1]
    else:
        ans+=ab[i][0]*(m-now_b)
        break
print(ans)