x,a,b=map(int,input().split())

if(b<=a):
    print('delicious')
elif(a<b and b<=a+x):
    print('safe')
else:
    print('dangerous')