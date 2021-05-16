m,n,N=map(int,input().split())
ans=N
pen=N
rest=0

while(True):
    if(pen<m):
        pen+=rest
        rest=0
        if(pen<m):
            break
    else:
        make=pen//m
        rest+=pen-m*make
        ans+=n*make
        pen=n*make
print(ans)
