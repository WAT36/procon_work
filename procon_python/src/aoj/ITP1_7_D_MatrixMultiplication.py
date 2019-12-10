n,m,l=map(int,input().split())
a=[]
b=[]

for i in range(n):
    a.append(list(map(int,input().split())))

for i in range(m):
    b.append(list(map(int,input().split())))

c=[]
for i in range(n):
    ci=[]
    for j in range(l):
        cij=0
        for k in range(m):
            cij+=a[i][k]*b[k][j]
        ci.append(cij)
    c.append(ci)

for i in range(len(c)):
    for j in range(len(c[i])):
        print(c[i][j],end="")

        if(j<len(c[i])-1):
            print(" ",end="")
    print()
