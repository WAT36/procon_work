n,m=map(int,input().split())
a=[]
for i in range(m):
    a.append(int(input()))
a=a[::-1]

ans_set=set([])
for i in range(m):
    ai=a[i]
    if(ai not in ans_set):
        print(ai)
        ans_set.add(ai)

for i in range(1,n+1):
    if(i not in ans_set):
        print(i)
        ans_set.add(i)

