l,x,y,s,d=map(int,input().split())

sd=d-s if d>=s else (l-s)+d
ans=(sd)/(x+y)

if(y>x):
    ds=s-d if s>=d else (l-d)+s
    ans=min(ans,(ds)/(y-x))
print(ans)