abc=list(map(int,input().split()))
abc.sort()
a,b,c = abc[0],abc[1],abc[2]

ans=0

ans+=c-b
c+-(c-b)
a+=(c-b)

if((c-a)%2==0):
    ans+=(c-a)//2
    print(ans)
else:
    ans+=-(-(c-a)//2)
    ans+=1
    print(ans)
