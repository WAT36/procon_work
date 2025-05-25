n=int(input())
a=list(map(int,input().split()))
ans=0
for i in range(n):
    b=a[i]-1
    if(i==a[b]-1):
        ans+=1
print(ans//2)
