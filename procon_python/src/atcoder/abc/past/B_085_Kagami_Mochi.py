n=int(input())
d=[]
for i in range(n):
    d.append(int(input()))
d=list(set(sorted(d)))
print(len(d))
