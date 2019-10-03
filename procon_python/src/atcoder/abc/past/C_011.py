import sys
n=int(input())
ng=[int(input()) for i in range(3)]
count=0
if(n in ng):
    print("NO")
    sys.exit()

while(count<=100 and n>0):
    if(n-3 not in ng):
        n-=3
        count+=1
    elif(n-2 not in ng):
        n-=2
        count+=1
    elif(n-1 not in ng):
        n-=1
        count+=1
    else:
        print("NO")
        sys.exit()
if(count>100):
    print("NO")
else:
    print("YES")