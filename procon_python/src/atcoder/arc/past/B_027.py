n=int(input())
s1=input()
s2=input()

d={}
str_num=[str(i) for i in range(10)]

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

uf=UnionFind_fast(26)
alphabet='ABCDEFGHIJKLMNOPQRSTUVWXYZ'
set_alphabet=set([])

for i in range(n):
#    print(s1[i],s2[i])
    if(s1[i] not in str_num and s2[i] not in str_num):
        set_alphabet.add(s1[i])
        set_alphabet.add(s2[i])
#        print(alphabet.index(s1[i]), alphabet.index(s2[i]),d)
        uf.unite(alphabet.index(s1[i]), alphabet.index(s2[i]))
        if(i==0):
            d[alphabet[uf.find(alphabet.index(s1[i]))]]=9
            d[alphabet[uf.find(alphabet.index(s2[i]))]]=9
        else:
#            print(alphabet[uf.find(alphabet.index(s1[i]))],s1[i],s2[i],d)
            root_di=min( d.get(alphabet[uf.find(alphabet.index(s1[i]))], 10),
                         d.get(s1[i], 10),
                         d.get(s2[i], 10))
            d[alphabet[uf.find(alphabet.index(s1[i]))]]=root_di
            d[alphabet[uf.find(alphabet.index(s2[i]))]]=root_di
#            print(s1[i],s2[i],alphabet[uf.find(alphabet.index(s1[i]))],alphabet[uf.find(alphabet.index(s2[i]))],d)
    elif(s1[i] not in str_num):
        set_alphabet.add(s1[i])
        d[alphabet[uf.find(alphabet.index(s1[i]))]]=1
    elif(s2[i] not in str_num):
        set_alphabet.add(s2[i])
        d[alphabet[uf.find(alphabet.index(s2[i]))]]=1

#print(d)
#print(set_alphabet)

root_set=set([])
for i in list(set_alphabet):
    root_set.add(alphabet[uf.find(alphabet.index(i))])

#print(root_set)
ans=1
for i in list(root_set):
    ans*=d[alphabet[uf.find(alphabet.index(i))]]
print(ans)
