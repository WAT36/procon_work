import sys
n=int(input())
a=list(map(int,input().split()))

max_v=[0 for _ in range(n+1)]

max_v[0]=1-a[0]
if(n==0 and a[0]==1):
    print(1)
    sys.exit()
elif(max_v[0]<=0 or a[-1]<=0):
    print(-1)
    sys.exit()
#print(0,max_v[0])

for i in range(1,n+1):
    max_v[i]=2*max_v[i-1] - a[i]
#    print(i,max_v[i])
    if(max_v[i]<=0 and i<n):
        print(-1)
        sys.exit()
#print(max_v)
ans=a[-1]
v=a[-1]
for i in range(n-1,-1,-1):
    if(v>2*max_v[i]):
        print(-1)
        sys.exit()
    v=min(v,max_v[i])
    v+=a[i]
    ans+=v
#    print(i,v,ans)
print(ans)