n,m,x,y=map(int,input().split())
xi=sorted(list(map(int,input().split())))
yi=sorted(list(map(int,input().split())))
if(max(xi[-1],x)<min(yi[0],y)):
    print("No War")
else:
    print("War")
