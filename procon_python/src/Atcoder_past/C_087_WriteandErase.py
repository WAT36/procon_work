N = int(input())

count = {}
ans = 0

for i in range(N):
    a = int(input())
    v = count.get(a,0)
    v = v+1
    if(v%2 == 0):
        ans = ans - 1
    else:
        ans = ans + 1
    count[a] = v

print(ans)