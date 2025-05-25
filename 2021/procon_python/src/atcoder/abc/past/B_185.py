n,m,t=map(int,input().split())
bat=n
nowtime=0
for i in range(m):
    a,b=map(int,input().split())

    downcount=a-nowtime
    bat-=downcount
    if(bat<=0):
        print('No')
        break

    upcount=b-a
    bat+=upcount
    if(bat>=n):
        bat=n
    nowtime=b
else:
    downcount=t-nowtime
    bat-=downcount
    if(bat<=0):
        print('No')
    else:
        print('Yes')

