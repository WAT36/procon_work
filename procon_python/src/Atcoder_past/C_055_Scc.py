N,M = map(int,input().split())

if(2*N < M):
    rest = M - 2*N
    rest_scc = rest//4
    print(N + rest_scc)
else:
    print(M//2)