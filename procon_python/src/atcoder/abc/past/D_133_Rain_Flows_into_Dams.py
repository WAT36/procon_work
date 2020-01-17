n=int(input())
a=list(map(int,input().split()))

x=[]
s=sum(a)
x.append(s-2*sum(a[1::2]))
for i in range(1,n-1):
    x.append(2*a[i-1]-x[i-1])
x.append(2*a[n-1]-x[0])
print(*x)
