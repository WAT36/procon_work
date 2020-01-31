hw1=list(map(int,input().split()))
hw2=list(map(int,input().split()))
if(hw1[0] in hw2  or  hw1[1] in hw2):
    print("YES")
else:
    print("NO")