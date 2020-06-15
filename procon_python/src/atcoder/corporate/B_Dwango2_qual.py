n=int(input())
k=list(map(int,input().split()))
l=[]
l.append(k[0])
for i in range(len(k)-1):
    l.append(min(k[i],k[i+1]))
l.append(k[-1])
print(*l)


