
#x^nを繰り返し二乗法で求める関数
#実際やると大きすぎる数を計算しようとしてエラーになりやすい

#実際に使うときは、MOD=10000007 などの剰余計算を組み込んで使うこと！
def repeated_square(x,n):
    #nを2進数で表して順序反転
    bit_n=bin(n)[2:][::-1]
#    print(bit_n)

    ans=1
    ni=x

    if(bit_n[0]=="1"):
        ans*=ni

    for i in range(1,len(bit_n)):
        ni*=ni

        #i桁目が1なら、x^(2^i)を加える
        if(bit_n[i]=="1"):
            ans*=ni
#            print(i,ni,ans)

    return ans


print(repeated_square(2,100))