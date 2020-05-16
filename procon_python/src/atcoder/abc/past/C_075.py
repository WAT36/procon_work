n,m=map(int,input().split())
e=[[] for _ in range(n+1)]
eab=[]
for i in range(m):
    a,b=map(int,input().split())
    e[a].append(b)
    e[b].append(a)
    eab.append([a,b])

def dfs(used,count,v):

    used[v]=True
    c=count+1
    ev=e[v]
    for ei in ev:
        if(used[ei]):
            continue
        else:
            c=dfs(used,c,ei)
    return c

ans=0
for i in range(m):
    a,b=eab[i]
    e[a].remove(b)
    e[b].remove(a)
    ci=dfs([False for _ in range(n+1)],0,1)
    if(ci!=n):
        ans+=1
    e[a].append(b)
    e[b].append(a)
print(ans)
