import math
ans=[]
while(True):
    n=int(input())
    if(n==0):
        break
    s=list(map(int,input().split()))
    ave=sum(s)/n
    diff_sum_bi=sum([(s[i]-ave)**2 for i in range(n)])
    variance=diff_sum_bi/n
    ans.append(math.sqrt(variance))

for i in range(len(ans)):
    print(ans[i])
