n=int(input())
a=list(map(int,input().split()))
subordinate=[0 for _ in range(n)]
for ai in a:
    subordinate[ai-1]+=1

for si in subordinate:
    print(si)

