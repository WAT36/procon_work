n,k=map(int,input().split())
MOD=(10**9)+7

ans=0
for i in range(k,n+2):
    min_sum=i*(i-1)//2
    max_sum=i*(n+(n-i+1))//2
#    print(i,min_sum,max_sum,max_sum-min_sum+1)
    ans=(ans+(max_sum-min_sum+1))%MOD
print(ans)