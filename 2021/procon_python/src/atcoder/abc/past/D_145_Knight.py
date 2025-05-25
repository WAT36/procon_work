import sys
MOD=(10**9) + 7
x,y=map(int,input().split())

if((x+y)%3!=0):
    print(0)
    sys.exit()

n=((x+y)//3) + 1
k=y-(n-2)

fac=[0 for _ in range(n)]   #n!
finv=[0 for _ in range(n)]  #1/n!
inv=[0 for _ in range(n)]   #

fac[0]=1
fac[1]=1
finv[0]=1
finv[1]=1
inv[1]=1

for i in range(2,n):
    fac[i]=fac[i-1]*i%MOD
    inv[i]=MOD - inv[MOD%i] * (MOD//i)%MOD
    finv[i]=finv[i-1]*inv[i]%MOD

def ncr(n,k):
    if(n < k):
        return 0
    elif(n < 0 or k < 0):
        return 0
    else:
        return fac[n] * (finv[k] * finv[n - k] % MOD) % MOD


print(ncr(n-1,k-1))