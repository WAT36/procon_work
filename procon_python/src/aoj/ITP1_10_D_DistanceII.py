import math
n=int(input())
x=list(map(int,input().split()))
y=list(map(int,input().split()))
p1=0
p2=0
p3=0
pinf=0

for i in range(n):
    p1+=abs(x[i]-y[i])
    p2+=abs(x[i]-y[i])**2
    p3+=abs(x[i]-y[i])**3
    pinf=max(pinf,abs(x[i]-y[i]))
p2=math.sqrt(p2)
p3=p3**(1/3)

print(p1)
print(p2)
print(p3)
print(pinf)
