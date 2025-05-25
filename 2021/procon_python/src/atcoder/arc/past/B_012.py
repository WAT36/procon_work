n,va,vb,l=map(int,input().split())
ans=l
for i in range(n):
    ans*=(vb/va)
print("{0:.7f}".format(ans))