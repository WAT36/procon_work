n,s,t=map(int,input().split())
w=0
ans=0
for i in range(n):
    w+=int(input())
    if(s<=w and w<=t):
        ans+=1
print(ans)