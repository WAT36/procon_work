# -*- coding:utf-8 -*-

# 素数に関するライブラリ群

#エラトステネスの篩  n以下の素数を列挙したリストを作る
def eratosthenes(n):
    prime_check=[True for _ in range(n+1)]
    prime_check[0]=False
    prime_check[1]=False
    prime=[]
    for i in range(2,n+1):
        if(prime_check[i]):
            prime.append(i)
            for j in range(i+i,n+1,i):
                prime_check[j]=False
    return prime


print(eratosthenes(100))