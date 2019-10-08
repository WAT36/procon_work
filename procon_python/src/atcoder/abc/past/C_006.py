import sys
n,m=map(int,input().split())
for z in range(n+1):
    x = 3*n - m + z
    y = m - 2*n - 2*z
    if(0<=x and 0<=y):
        print(str(x) + " " + str(y) + " " + str(z))
        sys.exit()
print(str(-1) + " " + str(-1) + " " + str(-1))