x,y=map(int,input().split())
x,y=max(x,y),min(x,y)
while(y!=0):
    x,y=y,x%y
print(x)
