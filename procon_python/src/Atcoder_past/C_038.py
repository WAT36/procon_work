N=int(input())
a=list(map(int,input().split()))
l=0
r=0
ans=0
for i in range(N):
    if(i != N-1 and a[i] < a[i+1]):
        r=i+1
    else:
        if(l != r):
            n = r-l+1
            ans += n * (n+1) // 2
        else:
            ans += 1
        l=i+1
        r=i+1
print(ans)