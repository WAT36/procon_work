N = int(input())

a = list(map(int,input().split()))

x = {}

for i in range(N):

    ai = a[i]

    temp = x.get(ai-1, 0)
    temp += 1
    x[ai-1] = temp

    temp = x.get(ai, 0)
    temp += 1
    x[ai] = temp

    temp = x.get(ai+1, 0)
    temp += 1
    x[ai+1] = temp

X = max(x.values())
print(X)
