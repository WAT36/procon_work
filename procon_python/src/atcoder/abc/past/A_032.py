import fractions
a,b,n=int(input()),int(input()),int(input())
print((a*b//fractions.gcd(a, b))*(-(-n // (a*b//fractions.gcd(a, b)))))