n=int(input())
h=list(map(int,input().split()))
ans=0
down=0
for i in range(n-1):
    if(h[i] >= h[i+1]):
        down+=1
    else:
        if(down > ans):
            ans = down
        down = 0
if(down > ans):
    ans = down
print(ans)