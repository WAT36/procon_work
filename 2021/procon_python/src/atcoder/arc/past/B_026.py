import math
n=int(input())
divisor=[]
for i in range(1,int(math.sqrt(n)//1)+1):
    if(n%i==0):
        divisor.append(i)
        divisor.append(n//i)
#print(divisor)
sum_div=sum(set(divisor))-n
if(sum_div<n):
    print("Deficient")
elif(sum_div>n):
    print("Abundant")
else:
    print("Perfect")