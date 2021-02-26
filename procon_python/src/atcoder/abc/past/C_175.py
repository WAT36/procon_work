x,k,d=map(int,input().split())
if(0 <= x-k*d):
    print(abs(x-k*d))
elif(x+k*d <= 0):
    print(abs(x+k*d))
else:
    a=(-1*x/d)//1

    if(k%2==0):
        while(a%2!=0):
            a-=1
    else:
        while(a%2!=1):
            a-=1

    print(min(int(abs(x+a*d)),int(abs(x+(a+2)*d))))
