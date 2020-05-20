n,s,t=map(int,input().split())
ans=0
w=int(input())
now_w=w
if(s<=now_w and now_w<=t):
    ans+=1

for i in range(n-1):
    a=int(input())
    now_w+=a
    if(s<=now_w and now_w<=t):
        ans+=1
print(ans)