n,t=map(int,input().split())
a=[]
b=[]
d=[]
for i in range(n):
    ai,bi=map(int,input().split())
    a.append(ai)
    b.append(bi)
    d.append(ai-bi)

if(sum(b)>t):
    print(-1)
else:
    suma=sum(a)
    d.sort(reverse=True)
    ans=0
    i=0
#    print(d)
    while(suma>t):
        suma-=d[i]
        i+=1
        ans+=1
    print(ans)