import sys
from collections import deque
h,w=map(int,input().split())
s=[]
wall_num=0
for i in range(h):
    s.append(list(input()))
    wall_num+=s[i].count("#")

q=deque()

i=0
j=0
s[0][0]=0
q.appendleft([0,0])
while(len(q)>0):
    qi=q.popleft()
    j,i=qi[0],qi[1]
    num=s[j][i]
    if(i==w-1 and j==h-1):
        print(h*w - wall_num - num - 1)
        sys.exit()
    if(i>0 and s[j][i-1]=="."):
        s[j][i-1]=num+1
        q.append([j,i-1])
    if(i<w-1 and s[j][i+1]=="."):
        s[j][i+1]=num+1
        q.append([j,i+1])
    if(j>0 and s[j-1][i]=="."):
        s[j-1][i]=num+1
        q.append([j-1,i])
    if(j<h-1 and s[j+1][i]=="."):
        s[j+1][i]=num+1
        q.append([j+1,i])

print(-1)