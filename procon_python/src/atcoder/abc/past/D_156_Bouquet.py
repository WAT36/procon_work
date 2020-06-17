n,a,b=map(int,input().split())
MOD  = 1000000007

def comb(N,x):
    numerator = 1
    for i in range(N-x+1,N+1):
        numerator = numerator *i%MOD
    denominator = 1
    for j in range(1,x+1):
        denominator = denominator *j%MOD
    d = pow(denominator,MOD-2,MOD)
    return (numerator*d)%MOD


#実際に使うときは、MOD=10000007 などの剰余計算を組み込んで使うこと！
def repeated_square(x,n):
    #nを2進数で表して順序反転
    bit_n=bin(n)[2:][::-1]

    ans=1
    ni=x

    if(bit_n[0]=="1"):
        ans*=ni

    for i in range(1,len(bit_n)):
        ni=((ni%MOD)*(ni%MOD))%MOD

        #i桁目が1なら、x^(2^i)を加える
        if(bit_n[i]=="1"):
            ans=((ans%MOD)*(ni%MOD))%MOD

    return ans

alln=(repeated_square(2, n)-1)%MOD
print((alln-comb(n, a)-comb(n, b))%MOD)
