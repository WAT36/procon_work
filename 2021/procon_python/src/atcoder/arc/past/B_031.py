import sys
import copy
a=[]
for i in range(10):
    a.append(list(input()))

def dfs(i,j):
    if(a[i][j]=="o"):
        a[i][j] = "z"
        if(j<9):
            dfs(i,j+1)
        if(0<i):
            dfs(i-1,j)
        if(0<j):
            dfs(i,j-1)
        if(i<9):
            dfs(i+1,j)

for i in range(10):
    for j in range(10):
        a_copy=copy.deepcopy(a)
        a[i][j]="o"
        dfs(i,j)

        flag=False
        for k in range(10):
            for l in range(10):
                if(a[k][l]=="o"):
                    flag=True
                    break
            if(flag):
                break
        if(not flag):
            print("YES")
            sys.exit()
        else:
            a=copy.deepcopy(a_copy)
print("NO")