import math
a,b,h,m=map(int,input().split())
m_theta=m*2*math.pi/60
h_theta=(h*60+m)*2*math.pi/720
theta=abs(m_theta-h_theta)
print(math.sqrt((a*a)+(b*b)-2*a*b*math.cos(theta)))