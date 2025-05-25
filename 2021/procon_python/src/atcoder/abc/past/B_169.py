n=int(input())
a=list(map(int,input().split()))
ans=a[0]
if(min(a)==0):
    print(0)
else:
    for i in range(1,n):
        ans*=a[i]
        if(ans>10**18):
            print(-1)
            break
    else:
        print(ans)