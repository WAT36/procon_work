x,y=map(int,input().split())
ans=0
prize=[300000,200000,100000]
if(x<=3):
    ans+=prize[x-1]
if(y<=3):
    ans+=prize[y-1]
if(x==1 and y==1):
    ans+=400000
print(ans)