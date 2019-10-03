import sys
import math
txa,tya,txb,tyb,t,v=map(int,input().split())
n=int(input())
min_d=9999999999
a=tyb-tya
b=-1*(txb-txa)
c=tya*(txb-txa) - txa*(tyb-tya)
for i in range(n):
    x,y=map(int,input().split())
    d=abs(a*x + b*y + c)//(math.sqrt(a*a + b*b)//1)
    if(min_d > d):
        dist= math.sqrt((x-txa)**2 + (y-tya)**2) + math.sqrt((txb-x)**2 + (tyb-y)**2)
        time=dist/v
        if(time <= t):
            print("YES")
            sys.exit()
print("NO")