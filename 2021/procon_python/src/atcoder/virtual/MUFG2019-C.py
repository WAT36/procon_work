import sys
x=int(input())

n=1
while(100*n<=x):
    if(x<=105*n):
        print(1)
        sys.exit()
    n+=1
print(0)
