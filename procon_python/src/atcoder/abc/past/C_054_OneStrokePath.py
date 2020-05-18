import copy
n,m=map(int,input().split())
g=[set([]) for _ in range(n+1)]
for i in range(m):
    a,b=map(int,input().split())
    g[a].add(b)
    g[b].add(a)

ans=0
def dfs(v,used):
    usedi=copy.deepcopy(used)
    usedi[v]=True

    nexti=g[v]
    for i in nexti:
        if(usedi[i]):
            continue
        else:
            dfs(i,usedi)

    if(usedi[1:].count(True) == n):
        global ans
        ans+=1

dfs(1,[False for _ in range(n+1)])
print(ans)