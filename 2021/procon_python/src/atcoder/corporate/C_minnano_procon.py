k,a,b=map(int,input().split())
bis=1

if(k<=a-1):
    print(k+1)
elif(b<a+2):
    print(k+1)
else:
    bis+=a-1

    rest=k-(a-1)
#    print(bis,rest)

    exc=rest//2

    bis=(exc*b - (exc-1)*a)

    if(rest%2==1):
        bis+=1

    print(bis)


