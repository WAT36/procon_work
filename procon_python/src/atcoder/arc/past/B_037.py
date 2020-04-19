import sys
sys.setrecursionlimit(10 ** 7)
n,m=map(int,input().split())
graph_list=[[] for _ in range(n)]

for i in range(m):
    u,v=map(int,input().split())
    graph_list[u-1].append(v-1)
    graph_list[v-1].append(u-1)

checked_v=[]

def dfs(i,parent,flg):
    checked_v.append(i)

    for gi in graph_list[i]:
        if(gi == parent):
            continue
        elif(gi in checked_v):
#            print(i,graph_i,checked_v,graph_list,end="")
#            print("False")
            return False
        else:
#            print(i,graph_i,checked_v,graph_list)
            flg = dfs(gi,i,flg)

    return flg


ans=0

for i in range(n):
    if(i in checked_v):
        continue
    elif(dfs(i,-1,True)):
#        print("dfs uses:{0}".format(i),checked_v)
        ans+=1
print(ans)
