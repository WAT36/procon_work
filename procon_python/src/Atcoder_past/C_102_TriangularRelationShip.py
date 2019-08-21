N,K = map(int,input().split())

k = []
half_k = []
for i in range(1,N+1):
    if(i%K == 0):
        k.append(i)
    elif(i%(K/2) == 0):
        half_k.append(i)

if(K%2 == 0):
    print((len(k) ** 3) + (len(half_k) ** 3))
else:
    print(len(k) ** 3)