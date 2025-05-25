import sys
n=int(input())
w=[]
w.append(input())
for i in range(n-1):
    wi=input()
    if(wi in w or w[-1][-1] != wi[0]):
        print("No")
        sys.exit()
    else:
        w.append(wi)
print("Yes")
