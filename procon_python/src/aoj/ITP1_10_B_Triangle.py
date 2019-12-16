import math
a,b,c=map(int,input().split())
rad=math.radians(c)
s=a*b*math.sin(rad)/2
print(s)
edge=math.sqrt(a**2 + b**2 - 2*a*b*math.cos(rad))
print(a+b+edge)
print(s*2/a)
