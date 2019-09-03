n,x=map(int,input().split())
a=list(map(int,input().split()))
ans=0
for i in range(1,n):
    if(a[i-1]+a[i]>x):
        if(a[i-1] > x):
            eat = (a[i-1] - x) + a[i]
            a[i] -= a[i]
            a[i-1] -= a[i-1] - x
            ans += eat
        else:
            eat = (a[i-1] + a[i]) - x
            a[i] -= eat
            ans += eat
print(ans)