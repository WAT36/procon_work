n,m=map(int,input().split())
n%=12
l=360*(m/60)
s=(360*n/12)+((360/12)*(m/60))
print(min(abs(l-s),360-abs(l-s)))