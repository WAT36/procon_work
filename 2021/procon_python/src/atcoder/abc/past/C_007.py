import queue
r,c=map(int,input().split())
sy,sx=map(int,input().split())
gy,gx=map(int,input().split())
m=[]
for i in range(r):
    m.append(input())
result=[[-1 for _ in range(c)] for _ in range(r)]
q=queue.Queue(-1)
q.put([sy,sx,0])

def bfs(y,x,num):
    if(y==gy and x==gx):
        print(num)
        return True
    if(x<=0 or c<x or y<=0 or r<y):
        return False
    if(m[y-1][x-1]=="#" or result[y-1][x-1]!=-1):
        return False
    result[y-1][x-1]=num
    q.put([y,x+1,num+1])
    q.put([y-1,x,num+1])
    q.put([y,x-1,num+1])
    q.put([y+1,x,num+1])
    return False

while(True):
    qi=q.get()
    if(bfs(qi[0],qi[1],qi[2])):
        break
