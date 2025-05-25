n=int(input())
a=[-1]
for _ in range(n):
    a.append(int(input()))

ans=0
i=1
pushed_i=set([])
while(True):
    pushed_i.add(i)
    i=a[i]
    ans+=1

    if(i==2):
        print(ans)
        break
    elif(i==1 or (i in pushed_i)):
        print(-1)
        break


