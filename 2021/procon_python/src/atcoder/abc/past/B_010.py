n=int(input())
a=list(map(int,input().split()))

ans=0
for i in range(n):
    ai=a[i]
    ansi=0
    while(ai%2==0 or (ai+1)%3==0):
        ai-=1
        ansi+=1
    ans+=ansi
print(ans)
