n=[]
for _ in range(3):
    n.append(int(input()))
sn=list(reversed(sorted(n)))
for i in range(3):
    print(sn.index(n[i])+1)