N=int(input())
a=[]
for i in range(N):
    a.append(int(input()))
a_set = list(set(a))
a_set.sort()

d = {}
for i,v in enumerate(a_set):
    d[v] = i

for i in range(N):
    print(d[a[i]])