from fractions import gcd
MOD=(10**9)+7
n=int(input())
a=list(map(int,input().split()))
a_lcm=a[-1]

for ai in a:
    a_lcm=(a_lcm*ai) // gcd(a_lcm, ai)

sum_b=0
for ai in a:
    bi=a_lcm//ai
    sum_b+=bi
print(sum_b%MOD)