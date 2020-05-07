x=int(input())

xi=100
ans=0
while(xi<x):
    xi+=(xi//100)
    ans+=1
print(ans)