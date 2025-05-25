n,k=map(int,input().split())
up_beforek=0
ai_pre=0
ans=0
for i in range(n):
    ai=int(input())
    if(ai_pre<ai):
        up_beforek+=1
    else:
        up_beforek=1

    if(up_beforek==k):
#        print(i,ai,up_beforek)
        ans+=1
        up_beforek-=1

    ai_pre=ai
print(ans)

