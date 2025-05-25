n=int(input())
a=list(map(int,input().split()))
a.sort()
ans=n
sum_former=sum(a)
for i in range(n-1,-1,-1):
    sum_former-=a[i]
    if(2*sum_former < a[i]):
        ans=n-i
        break

print(ans)
