n=int(input())
f=[0 for i in range(n)]
for i in range(n):
    fi=int("".join(list(input().split())),2)
    f[i] = fi
print(f)
p=[[] for i in range(n)]
for i in range(n):
    pi=list(map(int,input().split()))
    p[i] = pi
print(p)
ans=-9999999999999
for i in range(1,1024):
    bene=0
    for j in range(n):
        c = str(bin(i & f[j])).count("1")
        bene+=p[j][c]
    if(ans < bene):
        ans = bene
print(ans)