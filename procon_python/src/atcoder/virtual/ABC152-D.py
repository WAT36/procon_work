n=int(input())
ans=0
count=[[0 for _ in range(10)] for _ in range(10)]
for i in range(1,n+1):
    stri=str(i)
    count[int(stri[0])][int(stri[-1])]+=1

for i in range(10):
    print(count[i])
    for j in range(i,10):
        if(i==j):
            ans+=count[i][j]*count[j][i]
        else:
            ans+=2*(count[i][j]*count[j][i])

print(ans)
