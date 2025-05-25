class UnionFind_fast:
    def __init__(self,n):
        self.parent=[i for i in range(n)]
        self.rank=[0 for i in range(n)]

    #xの根を求める
    def find(self,x):
        if(self.parent[x]==x):
            return x
        else:
            self.parent[x] = self.find(self.parent[x])
            return self.parent[x]

    #xとyの属する集合を併合
    def unite(self,x,y):
        x=self.find(x)
        y=self.find(y)
        if(x==y):
            pass
        elif(self.rank[x] < self.rank[y]):
            self.parent[x] = y
        else:
            self.parent[y] = x
            if(self.rank[x] == self.rank[y]):
                self.rank[x]+=1

    #xとyが同じ集合に属するか判定
    def same(self,x,y):
        return self.find(x)==self.find(y)

n,m=map(int,input().split())
uf=UnionFind_fast(n+1)
for _ in range(m):
    a,b=map(int,input().split())
    uf.unite(a, b)

group=[]
for i in range(1,n+1):
    group.append(uf.find(i))
print(len(set(group))-1)

