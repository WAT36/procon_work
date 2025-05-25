from collections import deque
n=int(input())
g=[[] for _ in range(n+1)]
e=[]
for i in range(n-1):
    a,b=map(int,input().split())
    g[a-1].append(b-1)
    e.append(b-1)

q=deque([0])

color=[0 for _ in range(n)]
while(len(q)>0):
    ei=q.popleft()
    c=1
    for x in g[ei]:
        if c == color[ei]:
            c+=1

        color[x]=c
        c+=1
        q.append(x)
        print(color)

print(max(color))
for i in e:
    print(color[i])