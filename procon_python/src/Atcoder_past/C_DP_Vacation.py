N = int(input())
a = []
b = []
c = []

for i in range(N):
    x,y,z = [int(i) for i in input().split()]
    a.append(x)
    b.append(y)
    c.append(z)

dp_a = [-1] * N
dp_b = [-1] * N
dp_c = [-1] * N

dp_a[0] = a[0]
dp_b[0] = b[0]
dp_c[0] = c[0]

for i in range(1,N):
    dp_a[i] = dp_b[i-1] + a[i] if dp_b[i-1] > dp_c[i-1] else dp_c[i-1] + a[i]
    dp_b[i] = dp_a[i-1] + b[i] if dp_a[i-1] > dp_c[i-1] else dp_c[i-1] + b[i]
    dp_c[i] = dp_a[i-1] + c[i] if dp_a[i-1] > dp_b[i-1] else dp_b[i-1] + c[i]

print(max(dp_a[N-1],dp_b[N-1],dp_c[N-1]))
