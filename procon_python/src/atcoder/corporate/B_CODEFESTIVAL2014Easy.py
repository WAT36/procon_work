n=int(input())
if(n%40==0):
    print(1)
else:
    n%=40
    if(1<=n and n<=20):
        print(n)
    else:
        print(41-n)