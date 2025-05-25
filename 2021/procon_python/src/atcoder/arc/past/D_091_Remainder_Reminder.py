n,k=map(int,input().split())
ans=0
for i in range(k+1,n+1):
    ans_i=(i-k)*(-(-(n+1)//i))
#    print(i,ans_i,end=" ")
    if(n%i<k):
        ans_i-=(i-k)
    else:
        ans_i-=(i-1)-(n%i)
#    print(ans_i)
    ans+=ans_i

if(k==0):
    ans-=n
print(ans)