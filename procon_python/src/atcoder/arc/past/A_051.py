import math
x1,y1,r=map(int,input().split())
x2,y2,x3,y3=map(int,input().split())

def dist(x1,y1,x2,y2):
    d=math.sqrt((x2-x1)**2 + (y2-y1)**2)
    return d

if(dist(x1,y1,x2,y2)<=r and
   dist(x1,y1,x2,y3)<=r and
   dist(x1,y1,x3,y2)<=r and
   dist(x1,y1,x3,y3)<=r):
    print('YES')
    print('NO')
elif(abs(x1-x2)>=r and
     abs(x1-x3)>=r and
     abs(y1-y2)>=r and
     abs(y1-y3)>=r and
     x2<=x1 and x1<=x3 and y2<=y1 and y1<=y3):
    print('NO')
    print('YES')
else:
    print('YES')
    print('YES')