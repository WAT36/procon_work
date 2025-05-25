import math
x,y=map(int,input().split())
n=int(input())

ans=999999999999

def calc_d(x,y,xj,yj,xk,yk):
    a=0
    b=0
    c=0
    ans_j=0
    if(yk==yj):
        return abs(y-yk)
    elif(xk==xj):
        return abs(x-xk)
    else:
        a=(yk-yj)/(xk-xj)
        b=-1
        c=yk - a*xk
        ans_j=abs(a*x + b*y + c)/math.sqrt(a**2 + b**2)
    return ans_j


x0,y0=map(int,input().split())
xi=[x0]
yi=[y0]
for j in range(1,n):
    xj=xi[-1]
    yj=yi[-1]
    xk,yk=map(int,input().split())

    ans_j=calc_d(x, y, xj, yj, xk, yk)
    if(ans>ans_j):
        ans=ans_j

    xi.append(xk)
    yi.append(yk)
else:
    ans_j=calc_d(x, y, xi[-1], yi[-1], xi[0], yi[0])
    if(ans>ans_j):
        ans=ans_j

print(ans)
