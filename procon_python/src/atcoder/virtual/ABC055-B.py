n=int(input())
MOD=(10**9)+7
ans=1
for i in range(1,n+1):
    ans=((ans%MOD)*(i%MOD))%MOD
print(ans)