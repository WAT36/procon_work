s=list(input())
t=int(input())

y=s.count("U") - s.count("D")
x=s.count("L") - s.count("R")

q=s.count("?")
dist=abs(x)+abs(y)
if(t==1):
    print(dist+q)
else:
    print(dist-q if dist>=q else abs(dist-q)%2)
