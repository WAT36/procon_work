import math
N = int(input())
x=0
t=0
n=0
pre_t=1
pre_n=1
for i in range(N):
    t,n = map(int,input().split())
    if(pre_t > t or pre_n > n):
        mul = max(-(-pre_t//t),-(-pre_n//n))
        t *= mul
        n *= mul
    pre_t = t
    pre_n = n
    x = t+n
print(x)