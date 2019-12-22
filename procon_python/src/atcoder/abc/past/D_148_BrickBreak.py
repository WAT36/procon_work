n=int(input())
a=list(map(int,input().split()))
num=1
start=0
while(start != -1):
    try:
        start=a.index(num,start)
        num+=1
    except ValueError:
        break
num-=1
#print(n,num)
if(num>0):
    print(n-num)
else:
    print(-1)