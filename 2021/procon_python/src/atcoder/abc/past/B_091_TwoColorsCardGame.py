cardcost = {}
N = int(input())
for i in range(N):
    s = input()
    scost = cardcost.get(s, 0)
    cardcost[s] = scost+1

M = int(input())
for i in range(M):
    t = input()
    tcost = cardcost.get(t, 0)
    cardcost[t] = tcost-1


ans = max(cardcost.values())
if(ans > 0):
    print(ans)
else:
    print(0)
