n=int(input())
h=list(map(int,input().split()))
sum=0
flag=False
for i in range(max(h)+1):
    for j in range(n):
        if(h[j]>0):
            flag=True
            h[j]-=1
        elif(flag):
            sum+=1
            flag=False
    if(flag):
        sum+=1
    flag=False
print(sum)