a = list(map(int,input().split()))
order = [[0,1,2],[0,2,1],[1,0,2],[1,2,0],[2,0,1],[2,1,0]]
ans = 10000000
for i in range(len(order)):
    cost = abs(a[order[i][1]] - a[order[i][0]]) + abs(a[order[i][2]] - a[order[i][1]])
    if(ans > cost):
        ans = cost
print(ans)