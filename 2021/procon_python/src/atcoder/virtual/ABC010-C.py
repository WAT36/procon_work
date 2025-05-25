import math
txa,tya,txb,tyb,t,v=map(int,input().split())
n=int(input())
for i in range(n):
    x,y=map(int,input().split())
    a=math.sqrt(abs(x-txa)**2 + abs(y-tya)**2)
    b=math.sqrt(abs(x-txb)**2 + abs(y-tyb)**2)
    if((a+b)/v <= t):
        print('YES')
        break
else:
    print('NO')

