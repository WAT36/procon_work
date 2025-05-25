n,k=map(int,input().split())
ans=0
MOD=(10**9)+7

fact_ans=[1 for _ in range(n+1)]
for i in range(1,n+1):
    fact_ans[i]=fact_ans[i-1]*i

def fact(n):
    if(n<0):
        return 1
    else:
        return fact_ans[n]

for i in range(1,k+1):
    blue=fact(k-1)//(fact(k-i)*fact(i-1))
    red=( fact(n-k+1)//( fact(i)*fact(n-k+1-i))  )
    print((blue*red)%MOD)
