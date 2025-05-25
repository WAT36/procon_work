n=int(input())
ans=0
for i in range(n):
    ansi=sum(list(map(int,input().split())))
    if(0<=ansi and ansi<20):
        ans+=1
print(ans)