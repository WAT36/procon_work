n=int(input())
x=list(map(int,input().split()))
ans=9999999999
for i in range(min(x),max(x)+1):
    xi=list(map(lambda x:(x-i)**2,x))
    ans=min(ans,sum(xi))
print(ans)
