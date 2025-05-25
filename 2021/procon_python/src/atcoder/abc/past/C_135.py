n=int(input())
a=list(map(int,input().split()))
b=list(map(int,input().split()))

ans=0
for i in range(n):
    if(a[i]>b[i]):
        ans+=b[i]
    else:
        ans+=a[i]
        b[i]-=a[i]
        a[i]=0
        ans+=min(a[i+1],b[i])
        a[i+1]=max(a[i+1]-b[i],0)
print(ans)

