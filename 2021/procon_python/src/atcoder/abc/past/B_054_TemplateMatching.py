import sys
n,m=map(int,input().split())
a=[]
b=[]
for _ in range(n):
    a.append(input())

for _ in range(m):
    b.append(input())

for iy in range(n-m+1):
    for ix in range(n-m+1):
        bflag=True
        for jy in range(m):
            for jx in range(m):
#                print(iy,ix,jy,jx)
                if(a[iy+jy][ix+jx] != b[jy][jx]):
                    bflag=False
                    break
            if(not bflag):
                break
        else:
            print("Yes")
            sys.exit()

print("No")
