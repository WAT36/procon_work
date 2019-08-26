import math
N=int(input())

MOD = (10 ** 9) + 7

def factorization(n):
    x = 2
    pw = 0
    factlist = []
    while(n != 1):
        if(n%x == 0):
            n = n // x
            pw += 1
        elif(pw > 0):
            factlist.append([x,pw])
            pw = 0
            x += 1
        else:
            x += 1
    factlist.append([x,pw])
    return factlist


list = factorization(math.factorial(N))
ans = 1
for i in range(len(list)):
    ans = ((ans % MOD) * ( (list[i][1] + 1) % MOD)) % MOD
print(ans)