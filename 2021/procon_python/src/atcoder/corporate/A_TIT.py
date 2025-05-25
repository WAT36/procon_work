a,b,t = map(int,input().split())
x=(t-a)//(b-a)
if((t-a)%(b-a) == 0):
    print((b-a)*x+a)
else:
    print((b-a)*(x+1)+a)