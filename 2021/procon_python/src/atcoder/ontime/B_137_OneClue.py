num = list(map(int,input().split()))
K = num[0]
X = num[1]

for i in range(X-K+1,X+K):
    print(str(i) + " ",end="")

print()