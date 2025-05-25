import math
n=int(input())
ans=[]
for i in range(1,n+1,2):
    div=0
    for j in range(1,int(math.sqrt(i)//1)+1):
        if(i%j==0):
            div+=1

    if(div==4):
        ans.append(i)

print(len(ans))
