x=int(input())

def eratosthenes(n):
    prime_check=[True for _ in range(100010)]
    prime_check[0]=False
    prime_check[1]=False
    for i in range(2,n+1):
        j=2
        while(i*j<=n):
            prime_check[i*j]=False
            j+=1
        if(i*j<100010):
            prime_check[i*j]=False
    return prime_check


p=eratosthenes(x)
i=x
while(True):
    if(p[i]):
        print(i)
        break
    else:
        i+=1