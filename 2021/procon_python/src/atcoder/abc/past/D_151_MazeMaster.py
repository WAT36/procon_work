import copy
from collections import deque
h,w=map(int,input().split())
maze=[]
for i in range(h):
    maze.append(list(input()))


def dfs(start_h,start_w):
    q=deque()
    maze_copy=copy.deepcopy(maze)
    walk_count=[[0 for _ in range(w)] for _ in range(h)]
    q.append([start_h,start_w])
    maze_copy[start_h][start_w]="#"
    max_count=0
    while(len(q)!=0):
        position=q.popleft()
        now_h=position[0]
        now_w=position[1]
        now_count=walk_count[now_h][now_w]
        if(now_h>0 and maze_copy[now_h-1][now_w]=='.'):
            walk_count[now_h-1][now_w]=now_count+1
            maze_copy[now_h-1][now_w]="#"
            q.append([now_h-1,now_w])
            if(max_count<now_count+1):
                max_count=now_count+1

        if(now_h<h-1 and maze_copy[now_h+1][now_w]=='.'):
            walk_count[now_h+1][now_w]=now_count+1
            maze_copy[now_h+1][now_w]="#"
            q.append([now_h+1,now_w])
            if(max_count<now_count+1):
                max_count=now_count+1

        if(now_w>0 and maze_copy[now_h][now_w-1]=='.'):
            walk_count[now_h][now_w-1]=now_count+1
            maze_copy[now_h][now_w-1]="#"
            q.append([now_h,now_w-1])
            if(max_count<now_count+1):
                max_count=now_count+1

        if(now_w<w-1 and maze_copy[now_h][now_w+1]=='.'):
            walk_count[now_h][now_w+1]=now_count+1
            maze_copy[now_h][now_w+1]="#"
            q.append([now_h,now_w+1])
            if(max_count<now_count+1):
                max_count=now_count+1
    return max_count

ans=0
for i in range(h):
    for j in range(w):
        if(maze[i][j]=='.'):
            ij_count=dfs(i,j)
            if(ans<ij_count):
                ans=ij_count
print(ans)
