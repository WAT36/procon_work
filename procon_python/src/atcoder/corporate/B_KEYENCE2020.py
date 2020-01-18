n=int(input())
robots=[]
for i in range(n):
    x,l=map(int,input().split())
    robots.append([x-l,x+l])

robots.sort(key=lambda x:x[1])
now_d=-9999999999999999999
ans=0
for ri in robots:
    if(now_d<=ri[0]):
        ans+=1
        now_d=ri[1]
print(ans)