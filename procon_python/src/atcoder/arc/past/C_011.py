f,l=input().split()
n=int(input())
s=[f]
for i in range(n):
    s.append(input())
s.append(l)

g=[set([]) for _ in range(len(s))]

def canchange(s1,s2):
    ans=0
    for i in range(len(s1)):
        if(s1[i]!=s2[i]):
            ans+=1
        if(ans>1):
            return False

    if(ans<=1):
        return True
    else:
        return False

for i in range(len(s)-1):
    for j in range(i+1,len(s)):
        if(canchange(s[i], s[j])):
            g[i].add(j)
            g[j].add(i)

def dijkstra(start):
    pre=[-1 for i in range(len(s))]
    post=[-1 for i in range(len(s))]
    used=[False for i in range(len(s))]
    dist=[float("inf") for i in range(len(s))]

    dist[start]=0

    while(True):
        v=-1
        for u in range(len(s)):
            if(not used[u] and ( v==-1 or dist[u]<dist[v] )):
                v = u
        if(v==-1):
#             print(pre)
#             print(post)
#             print(used)
#             print(dist)
            return pre

        used[v]=True

        for u in range(len(s)):
            if(u in g[v] and dist[u]>=dist[v]+1):
                dist[u] = dist[v]+1
                pre[u] = v
                post[v] = u

route=dijkstra(0)

i=len(s)-1
ans=[]
count=0
while(True):
   ans.append(s[i])
   i=route[i]
   count+=1

   if(i==-1 or count>len(s)):
       break

ans=ans[::-1]
if(ans[-1]!=l or count>len(s)):
    print(-1)
else:
    print(len(ans)-2)
    for i in range(len(ans)):
        print(ans[i])
