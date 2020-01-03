#シェルソート　コメント部分のロジックでなぜダメなのかわからない
import re
def insertionSort(A,n,g):
    cnt=0
    for i in range(g,n):
        v = A[i]
        j = i-g
        while(j>=0 and A[j]>v):
            A[j+g] = A[j]
            j = j-g
            cnt+=1
        A[j+g]=v
    return cnt

def shellSort(A,n):
    cnt=0
#    m=n//2
#    print(m)
#    G=[]
#    while(m>0):
#        G.append(m)
#        m//=2

    G=[]
    v=1
    c=1
    while(v<=n):
        G.append(v)
        v+=3**c
        c+=1
    G=list(reversed(G))
    m=len(G)
    print(m)

    print(re.sub("[\[\]\,]","",str(G)))
    for i in range(len(G)):
        cnt+=insertionSort(A,n,G[i])
    print(cnt)


n=int(input())
a=[]
for i in range(n):
    a.append(int(input()))

shellSort(a,n)

for i in range(len(a)):
    print(a[i])
