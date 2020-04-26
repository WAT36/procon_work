#nCr 組み合わせ計算

N    = int(input())  #最大値入力
k    = int(input())
MOD  = 1000000007

fac=[]      #fac[n] = (n! mod p)
finv=[]     #finv[n]= ((n!)^-1 mod p)
inv=[]      #inv[n] = finv計算用

#前処理、初期化
def comInit(n,mod):
    fac.append(1)   #fac[0]
    fac.append(1)   #fac[1]
    finv.append(0)  #finv[0]
    finv.append(1)  #finv[1]
    inv.append(0)   #inv[0]
    inv.append(1)   #inv[1]
    for i in range(2,n+1):
        fac.append(fac[-1]*i%mod)
        inv.append(mod - inv[mod%i]*(mod//i)%mod)
        finv.append(finv[-1]*inv[i]%mod)

#二項係数計算
def comCalc(n,k):
    if(n<k):
        return 0
    elif(n<0 or k<0):
        return 0
    else:
        return fac[n]*(finv[k]*finv[n-k]%MOD)%MOD


comInit(N, MOD)
comCalc(N, k)
