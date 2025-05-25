n=int(input())
a=list(map(int,input().split()))
MOD=1000000007
hats=[0,0,0]
ans=1
for i in range(n):
    ai=a[i]
    ans=((ans%MOD)*hats.count(ai))%MOD
    if(ans==0):
        break
    hats[hats.index(ai)]+=1
#    print(ai,ans,hats)
print(ans%MOD)
