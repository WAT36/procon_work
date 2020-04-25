n,m,k=map(int,input().split())

class UnionFind:
    def __init__(self,n):
        self.group=[i for i in range(n)]
        self.size=[1 for i in range(n)]

    def find(self,x):
        if(self.group[x]==x):
            return x
        else:
            return self.find(self.group[x])

    def unite(self,x,y):
        x=self.find(x)
        y=self.find(y)
        if(x==y):
            pass
        elif(self.sizeof(y) > self.sizeof(x)):
            self.group[x] = self.group[y]
            self.size[y] += self.size[x]
            self.size[x]=0
        else:
            self.group[y] = self.group[x]
            self.size[x] += self.size[y]
            self.size[y]=0

    def sizeof(self,a):
        return self.size[self.find(a)]

    def same(self,x,y):
        return self.find(x)==self.find(y)

uf=UnionFind(n)
friends=[0 for _ in range(n)]
blocks=[0 for _ in range(n)]


for i in range(m):
    a,b=map(int,input().split())
    a-=1
    b-=1
    friends[a]+=1
    friends[b]+=1
    uf.unite(a,b)

for i in range(k):
    c,d=map(int,input().split())
    c-=1
    d-=1
    if(uf.same(c, d)):
        blocks[c]+=1
        blocks[d]+=1

ans=[]
for i in range(n):
    ans.append(uf.sizeof(i) - friends[i] - blocks[i]  - 1)
print(*ans)
