# -*- coding:utf-8 -*-

import math

i = list(map(int,input().split()))
N = i[0]
M = i[1]

MOD = 1000000000 + 7

diff = abs(max(M,N) - min(M,N))

if diff >= 2:
    print(0)
elif diff == 1:
    ans = (math.factorial(max(M,N)) % MOD) * (math.factorial(min(M,N)) % MOD)
    print(ans % MOD)
else:
    ans = (math.factorial(max(M,N)) % MOD) * (math.factorial(min(M,N)) % MOD) * 2
    print(ans % MOD)
