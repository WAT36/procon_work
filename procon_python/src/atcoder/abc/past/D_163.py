MOD=(10**9)+7
n,k=map(int,input().split())
ans=0
for i in range(k,n+2):
    min_start=0
    min_end=min_start+i-1
    max_end=n
    max_start=n-i+1
    min_sum=(min_end-min_start+1)*(min_end+min_start)//2
    max_sum=(max_end-max_start+1)*(max_end+max_start)//2
#    print(i,min_start,min_end,min_sum,max_start,max_end,max_sum,max_sum-min_sum+1)
    ans+=max_sum-min_sum+1
    ans=ans%MOD
print(ans%MOD)