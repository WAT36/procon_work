n,k=map(int,input().split())
a=list(map(int,input().split()))
i_sum=sum(a[0:k])
ans=i_sum
for i in range(1,n-k+1):
    i_sum-=a[i-1]
    i_sum+=a[i+k-1]
    ans+=i_sum
print(ans)