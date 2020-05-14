n,m=map(int,input().split())
i=1
x=[]
while(i*i<=m):
    if(m%i==0):
        x.append(i)
        x.append(m//i)
    i+=1
x.sort()
for xi in x:
    if(xi>=n):
        print(m//xi)
        break