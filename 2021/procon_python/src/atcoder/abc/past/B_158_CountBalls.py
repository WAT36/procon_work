n,a,b=map(int,input().split())
x=n-(n//(a+b))*(a+b)
if(x<=a):
    print((n//(a+b))*a + x)
else:
    print((n//(a+b))*a + a)