import fractions
a,b=map(int,input().split())
gcd_ab=fractions.gcd(a, b)

def prime_factorize(n):
    a = []
    while n % 2 == 0:
        a.append(2)
        n //= 2
    f = 3
    while f * f <= n:
        if n % f == 0:
            a.append(f)
            n //= f
        else:
            f += 2
    if n != 1:
        a.append(n)
    return a

ans=1
ans+=len(set(prime_factorize(gcd_ab)))
print(ans)