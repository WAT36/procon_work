import math
n=int(input())
for i in range(2,int(math.sqrt(n)//1)+1):
    if(n%i==0):
        print("NO")
        break
else:
    print("YES")
