from collections import deque

class Node:
    def __init__(self,idx,parent,child,depth):
        self.idx=idx
        self.parent=parent
        self.child=child
        self.depth=depth

n=int(input())

nodes=[Node(-1,-1,-1,-1) for _ in range(n)]

for i in range(n):
    id,k,*c=map(int,input().split())
    nodei=nodes[id]
    nodei.idx=id
    nodei.child=c
    for ci in c:
        nodes[ci].parent=id

q=deque()
root_i=-1
for ni in nodes:
    if(ni.parent==-1):
        root_i=ni.idx
        break

q.append([root_i,0])
while(len(q)>0):
    qi=q.popleft()
    node_idx=qi[0]
    node_depth=qi[1]
    nodes[node_idx].depth=node_depth
    node_child=nodes[node_idx].child
    for c in node_child:
        q.append([c,node_depth+1])


for nodei in nodes:
    print("node "+str(nodei.idx)+": ",end="")
    print("parent = "+str(nodei.parent)+", ",end="")
    print("depth = "+str(nodei.depth)+", ",end="")
    if(nodei.parent==-1):
        print("root, ",end="")
    elif(nodei.child==-1 or len(nodei.child)==0):
        print("leaf, ",end="")
    else:
        print("internal node, ",end="")
    print(nodei.child)



