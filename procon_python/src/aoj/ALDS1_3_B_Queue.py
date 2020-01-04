from collections import deque
robin=deque()

n,q=map(int,input().split())

for i in range(n):
    p,t=input().split()
    robin.append([p,int(t)])

time=0
while(len(robin)!=0):
    proc=robin.popleft()
    if(proc[1]<=q):
        print(proc[0],time+proc[1])
        time+=proc[1]
    else:
        proc[1]-=q
        robin.append(proc)
        time+=q

