import sys
sys.setrecursionlimit(10**7)
def dfs(i, j):
    if(c[i][j] != "1"):
        return 1
    else:
        c[i][j] = "2"

        if(0 < i):                      dfs(i - 1, j)
        if(0 < j):                      dfs(i, j - 1)
        if(i < h - 1):                  dfs(i + 1, j)
        if(j < w - 1):                  dfs(i, j + 1)
        if(0 < i and 0 < j):            dfs(i - 1, j - 1)
        if(0 < i and j < w - 1):        dfs(i - 1, j + 1)
        if(i < h - 1 and 0 < j):        dfs(i + 1, j - 1)
        if(i < h - 1 and j < w - 1):    dfs(i + 1, j + 1)
        return 1

ans=[]
while(True):
    islands=0
    w, h = map(int, input().split())
    if(w == 0 and h == 0):
        break
    c = []
    for i in range(h):
        c.append(input().split())
    for i in range(h):
        for j in range(w):
            if(c[i][j] == "1"):
                islands += dfs(i, j)
    ans.append(islands)

for i in range(len(ans)):
    print(ans[i])