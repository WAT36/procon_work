import bisect
n=int(input())
a=list(map(int,input().split()))
b=list(map(int,input().split()))

if(sum(a)<sum(b)):
    print(-1)
else:
    d=[a[i]-b[i] for i in range(n)]
    d.sort()

    ans=0
    minus_num=bisect.bisect_left(d, 0)
    ans+=minus_num
    minus_sum=sum(d[:minus_num])

    i=n-1
    while(minus_sum<0 and minus_num<=i):
        minus_sum+=d[i]
        i-=1
        ans+=1

    print(ans)