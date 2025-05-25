n,m=map(int,input().split())
friends=[[] for i in range(n+1)]
for i in range(m):
    a,b=map(int,input().split())
    friends[a].append(b)
    friends[b].append(a)
for i in range(1,n+1):
    sum_i=[]
    fofi =friends[i]
    for j in range(len(fofi)):
        sum_i.extend(friends[fofi[j]])
    sum_i = list(set(sum_i))
    if(i in sum_i):
        sum_i.remove(i)
    sum_i = list(set(sum_i) - set(fofi))
    print(len(sum_i))
