#速度重視、蟻本にあるやつ
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

#Union-findでそれぞれのグループのノードの個数を知りたい時
class UnionFind_size:
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
        print(x,y,self.group,self.size)
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
        print(x,y,self.group,self.size)

    #aが属するグループのサイズを取得
    def sizeof(self,a):
        return self.size[self.find(a)]

    #xとyが同じ集合に属するか判定
    def same(self,x,y):
        return self.find(x)==self.find(y)