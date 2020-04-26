n,m=map(int,input().split())

class UnionFind:
    def __init__(self,n):
        #ノードiの根(=どのグループに属するか)
        self.group=[i for i in range(n)]
        #ノードiを根に持つグループのサイズ(根でない要素は0)
        self.size=[1 for i in range(n)]

    #xの根を求める
    def find(self,x):
        if(self.group[x]==x):
            return x
        else:
            self.group[x] = self.find(self.group[x])
            return self.group[x]

    #xとyの属する集合を併合
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

    #aが属するグループのサイズを取得
    def sizeof(self,a):
        return self.size[self.find(a)]

    #xとyが同じ集合に属するか判定
    def same(self,x,y):
        return self.find(x)==self.find(y)

uf=UnionFind(n)

for i in range(m):
    a,b=map(int,input().split())
    a-=1
    b-=1
    uf.unite(a,b)

print(len(uf.size)-uf.size.count(0)-1)

