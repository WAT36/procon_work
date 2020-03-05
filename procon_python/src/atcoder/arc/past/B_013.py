c=int(input())
n=[]
m=[]
l=[]
for i in range(c):
    nml=sorted(list(map(int,input().split())))
    n.append(nml[0])
    m.append(nml[1])
    l.append(nml[2])
print(max(n)*max(m)*max(l))
