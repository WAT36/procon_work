import sys
M,D = map(int,input().split())

ans = 0
if(D < 20):
    print(0)
    sys.exit()

for i in range(1,M+1):
    for j in range(20,D+1):
        d10 = j//10
        d1  = j%10
        if(d1 < 2):
            continue
        elif(i == d10 * d1):
            ans += 1
print(ans)