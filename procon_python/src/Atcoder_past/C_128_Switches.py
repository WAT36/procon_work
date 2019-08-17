N,M = map(int,input().split())

x = 2 ** N

ks = []
for i in range(M):
    ks.append(list(map(int,input().split())))

p = list(map(int,input().split()))

ans = 0

for i in range(x):
    str_i = str(bin(i))[2:].zfill(N)
    flag = True
    for j in range(M):
        ks_j = ks[j]
        on_sum = 0
        for k in range(ks_j[0]):
            if(str_i[ks_j[k+1]-1] == '1'):
                on_sum += 1
        if(on_sum % 2 != p[j]):
            flag = False
            break
    if(flag):
        ans += 1

print(ans)