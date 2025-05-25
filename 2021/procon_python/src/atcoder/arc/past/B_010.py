n=int(input())
day=[False for _ in range(366)]
day[0]=True
sat=6
while(sat<366):
    day[sat]=True
    day[sat+1]=True
    sat+=7

days=[31,29,31,30,31,30,31,31,30,31,30,31]

for i in range(n):
    m,d=map(int,input().split('/'))
#    print(m,d)
    sumday=sum(days[:m-1])+(d-1)
    while(day[sumday] and sumday<365):
        sumday+=1
    day[sumday]=True
#print(day)
ans=0
ansi=0
for i in range(len(day)):
    if(day[i]):
        ansi+=1
    elif(ansi>0):
        if(ans<ansi):
            ans=ansi
        ansi=0
else:
    if(ans<ansi):
        ans=ansi
print(ans)

