n,x=map(int,input().split())
m=[]
ans=0
for i in range(n):
    m.append(int(input()))

x-=sum(m)
ans+=n

ans+=x//min(m)
print(ans)
