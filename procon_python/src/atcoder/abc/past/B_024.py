n,t=map(int,input().split())
pre_a=int(input())
ans=0
for _ in range(1,n):
    a=int(input())
    diff=a-pre_a
    if(diff<t):
        ans+=diff
    else:
        ans+=t
    pre_a=a
ans+=t
print(ans)
