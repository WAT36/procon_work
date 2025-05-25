a=int(input())
b=int(input())
c=int(input())
x=int(input())

ans=0
i=0
j=0
while(i<=a and i*500<=x):
    while(j<=b and (i*500 + j*100) <=x):
        rest=x-i*500-j*100
        if(rest%50==0):
            k=rest//50
            if(0<=k and k<=c):
#                print(i,j,k)
                ans+=1
        j+=1
    i+=1
    j=0
print(ans)