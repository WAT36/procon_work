n=int(input())
a=list(map(int,input().split()))
a.sort(reverse=True)
ans=a[0]
ans+=2*sum(a[1:1+((n-2)//2)])
if((n-2)%2==1):
    ans+=a[ -(-(n-2)//2) ]
print(ans)
