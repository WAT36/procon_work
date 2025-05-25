from collections import deque

class binaryNode:
    def __init__(self):
        self.num=-1
        self.parent=-1
        self.brother=-1
        self.child=[]
        self.degree=-1
        self.depth=-1
        self.high=-1
        self.type="-1"


n=int(input())
nodes=[binaryNode() for _ in range(n)]

for _ in range(n):
    idx,left,right=map(int,input().split())
    nodes[idx].num=idx
    child=[]
    if(left!=-1):
        nodes[left].parent=idx
        nodes[left].brother=right
        child.append(left)

    if(right!=-1):
        nodes[right].parent=idx
        nodes[right].brother=left
        child.append(right)

    nodes[idx].child=child
    nodes[idx].degree=len(child)

root_id=-1
for i in range(n):
    if(nodes[i].parent==-1):
        root_id=i
        break

q=deque()
q.append([root_id,0])
while(len(q)>0):
    qi=q.popleft()
    idx=qi[0]
    nodes[idx].depth=qi[1]
    children=nodes[idx].child

    if(nodes[idx].parent==-1):
        nodes[idx].type="root"
    elif(nodes[idx].degree==0):
        nodes[idx].type="leaf"
        nodes[idx].high=0
    else:
        nodes[idx].type="internal node"

    for c in children:
        q.append([c,qi[1]+1])

q.append(root_id)
while(len(q)>0):
    idx=q.popleft()
    children=nodes[idx].child
    children_high=[]
    for c in children:
        if(nodes[c].high==-1):
            q.append(c)
        else:
            children_high.append(nodes[c].high)

    if(len(children)==len(children_high)):
        if(len(children_high)==0):
            nodes[idx].high=0
        else:
            nodes[idx].high=max(children_high)+1
    else:
        q.append(idx)



for i in range(n):
    print("node "+str(i)+": parent = "+str(nodes[i].parent)+", sibling = "+str(nodes[i].brother)+", degree = "+str(nodes[i].degree)+", depth = "+str(nodes[i].depth)+", height = "+str(nodes[i].high)+", "+nodes[i].type)
