def isLineSegmentInterSected(p1x,p1y,p2x,p2y,p3x,p3y,p4x,p4y):
    if(((p1x - p2x) * (p3y - p1y) + (p1y - p2y) * (p1x - p3x)) *
       ((p1x - p2x) * (p4y - p1y) + (p1y - p2y) * (p1x - p4x)) < 0):
        if(((p3x - p4x) * (p1y - p3y) + (p3y - p4y) * (p3x - p1x)) *
           ((p3x - p4x) * (p2y - p3y) + (p3y - p4y) * (p3x - p2x)) < 0):
            return True
    return False

ax,ay,bx,by=map(int,input().split())
n=int(input())
points=[list(map(int,input().split()))]
intersected_num=0
for i in range(n-1):
    points.append(list(map(int,input().split())))
    if(isLineSegmentInterSected(points[-2][0],points[-2][1],points[-1][0],points[-1][1],ax,ay,bx,by)):
        intersected_num+=1
else:
    if(isLineSegmentInterSected(points[-1][0],points[-1][1],points[0][0],points[0][1],ax,ay,bx,by)):
        intersected_num+=1

print((intersected_num//2)+1)

