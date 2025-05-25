n,d=map(int,input().split())
ans=0
for i in range(n):
    xi,yi=map(int,input().split())
    if(d*d >= xi*xi + yi*yi):
        ans+=1
print(ans)