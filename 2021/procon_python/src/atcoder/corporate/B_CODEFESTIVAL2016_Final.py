import math
n=int(input())

#temp_n=int(math.sqrt(2*n)//1)-1
temp_n=int((-1+math.sqrt(1+8*n))//2)
#print(n,temp_n)

while(temp_n*(temp_n+1) < 2*n):
    temp_n+=1

#print(n,temp_n)
ans=[]
while(n>0):
#    print(n,temp_n,ans)
    if(n>=temp_n):
        n-=temp_n
        ans.append(temp_n)
        temp_n-=1
    else:
        temp_n=n
        ans.append(temp_n)
        n-=temp_n
ans.sort()

for ai in ans:
    print(ai)
