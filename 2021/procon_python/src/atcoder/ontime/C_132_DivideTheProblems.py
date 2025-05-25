n = int(input())
d = list(map(int,input().split()))

d.sort()

a = (int)((n/2) - 1)
b = (int)(n/2)

ans = d[b] - d[a]
print(ans)