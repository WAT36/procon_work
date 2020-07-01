n=int(input())
a=[]
b=[]
for i in range(n):
    ai,bi=map(int,input().split())
    a.append(ai)
    b.append(bi)

ab=[a[i]+b[i] for i in range(n)]

ab.sort(reverse=True)
asum=sum(ab[::2])
print(asum-sum(b))



