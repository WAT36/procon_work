n,a,b=map(int,input().split())
x=list(map(int,input().split()))
ans=0
pre_x=x[0]
for i in range(1,n):
    xi=x[i]
    if((xi-pre_x)*a >= b):
        ans+=b
    else:
        ans+=(xi-pre_x)*a
    pre_x=xi
print(ans)