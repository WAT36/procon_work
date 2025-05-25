n = int(input())
p = list(map(int,input().split()))

ans = 0

for i in range(0,len(p)-2):
    if( (max(p[i],p[i+1],p[i+2]) != p[i+1]) and min(p[i],p[i+1],p[i+2]) != p[i+1] ):
        ans+=1

print(ans)