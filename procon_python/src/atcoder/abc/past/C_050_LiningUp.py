import sys

MOD = 1000000007

N = int(input())
a = list(map(int,input().split()))

if(N%2 == 0):
    a.sort()
    for i in range(N//2):
        n = 2*i + 1
        if(a[2*i] != n or a[2*i + 1] != n):
            print(0)
            sys.exit()
    print((2 ** (N//2)) % MOD)
else:
    a.sort()
    if(a.count(0) != 1):
        print(0)
        sys.exit()
    for i in range((N-1)//2):
        n = 2*i + 2
        if(a[2*i + 1] != n or a[2*i + 2] != n):
            print(0)
            sys.exit()
    print((2 ** ((N-1)//2)) % MOD)
