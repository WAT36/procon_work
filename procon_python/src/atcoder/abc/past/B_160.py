x=int(input())
supa=x//500
ans=1000*supa
x-=500*supa
supb=x//5
ans+=5*supb
print(ans)