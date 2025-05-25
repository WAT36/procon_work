import sys
sys.setrecursionlimit(10**7)

h,w=map(int,input().split())
c=[]
sx=0
sy=0
for i in range(h):
    s=input()
    if("s" in s):
        sy=i
        sx=s.index("s")
    c.append(s)
r=[[False for _ in range(w)] for _ in range(h)]

def dfs(x,y):
    if(x<0 or w<=x or y<0 or h<=y):
        return False

    if(c[y][x] == "#" or r[y][x]):
        return False

    r[y][x] = True

    if(c[y][x]=="g"):
        return True

    if(dfs(x+1,y)):
        return True

    if(dfs(x-1,y)):
        return True

    if(dfs(x,y+1)):
        return True

    if(dfs(x,y-1)):
        return True

    return False

ans=dfs(sx,sy)
if(ans):
    print("Yes")
else:
    print("No")