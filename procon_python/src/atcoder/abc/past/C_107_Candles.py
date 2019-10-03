N,K = map(int,input().split())
x = list(map(int,input().split()))

ans = 100000000000
for i in range(N-K+1):
    dist = min(abs(x[i]),abs(x[i+K-1])) + abs(x[i+K-1] - x[i])
    if(dist < ans):
        ans = dist

print(ans)

