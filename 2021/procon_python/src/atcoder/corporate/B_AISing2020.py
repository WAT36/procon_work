n=int(input())
a=list(map(int,input().split()))
ans=0
for i in range(n):
    if((i+1)%2==1 and a[i]%2==1):
        ans+=1
print(ans)