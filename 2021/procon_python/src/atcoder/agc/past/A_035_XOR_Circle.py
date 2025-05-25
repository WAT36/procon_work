import sys
n=int(input())
a=list(map(int,input().split()))
if(len(set(a))==1 and a[0]==0):
    print("Yes")
elif(n%3!=0):
    print("No")
else:
    seta=list(set(a))
    nums=len(set(a))
    if(nums>3):
        print("No")
    elif(nums==3):
        if(a.count(seta[0])==n//3 and a.count(seta[1])==n//3 and a.count(seta[2]) and (seta[0] ^ seta[1] ^ seta[2] == 0)):
            print("Yes")
        else:
            print("No")
    elif(nums==2):
        seta.sort()
        if(seta[0]==0 and a.count(seta[0])==n//3):
            print("Yes")
        else:
            print("No")
    elif(nums==1):
        if(seta[0]==0):
            print("Yes")
        else:
            print("No")
