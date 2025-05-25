import sys
n=int(input())
s=input()
if(n%2==0):
    print(-1)
else:
    center=((n+1)//2)-1
    now=0
    while(center+now < n):
        if(now%3==0 and (s[center-now]!='b' or s[center+now]!='b')):
            print(-1)
            sys.exit()
        elif(now%3==1 and (s[center-now]!='a' or s[center+now]!='c')):
            print(-1)
            sys.exit()
        elif(now%3==2 and (s[center-now]!='c' or s[center+now]!='a')):
            print(-1)
            sys.exit()
        now+=1
    print(center)