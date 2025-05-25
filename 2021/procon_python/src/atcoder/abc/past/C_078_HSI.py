N,M = map(int,input().split())
ans = ((1900*M) + (N-M)*100)*(2**M)
print(ans)