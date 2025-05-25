from collections import deque
import sys
sys.setrecursionlimit(10**9)

n,q=map(int,input().split())

link=[[] for _ in range(n)]
for _ in range(n-1):
    a,b=map(int,input().split())
    link[a-1].append(b-1)
    link[b-1].append(a-1)

v_counter=[0 for _ in range(n)]
for _ in range(q):
    p,x=map(int,input().split())
    v_counter[p-1]+=x

point=[0 for _ in range(n)]
que=deque()
que.append(0)
used=set()
used.add(0)
point[0] += v_counter[0]

while(len(que)>0):
    ind=que.popleft()
    relate=link[ind]
    for i in relate:
        if(i in used):
            continue
        else:
            point[i] += point[ind] + v_counter[i]
            que.append(i)
            used.add(i)

print(*point)
