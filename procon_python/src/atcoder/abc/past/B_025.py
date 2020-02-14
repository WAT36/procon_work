n,a,b=map(int,input().split())
now=0
for _ in range(n):
    s,d=input().split()
    d=int(d)

    if(d<a):
        d=a
    elif(b<d):
        d=b

    if(s=='East'):
        now+=d
    elif(s=='West'):
        now-=d

if(now>0):
    print("East " + str(now))
elif(now<0):
    print("West " + str(abs(now)))
else:
    print(0)
