a,b=map(int,input().split())
i=0
while(True):
    xa=int(i*0.08)
    xb=int(i*0.10)
    if(xa==a and xb==b):
        print(i)
        break
    elif(xa>a and xb>b):
        print(-1)
        break
    else:
        i+=1
