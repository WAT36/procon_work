import math
a,b,x=map(int,input().split())
if(x > a*a*b/2):
    tanr=(2*b)/a - (2*x)/(a**3)
    print(math.degrees(math.atan(tanr)))
else:
    tanr=(a*b*b)/(2*x)
    print(math.degrees(math.atan(tanr)))