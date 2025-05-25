import bisect
n=int(input())
l=sorted(list(map(int,input().split())))
ans=0
for i in range(n-1):
    for j in range(i+1,n):
        min_c=j+1
        max_c=bisect.bisect_left(l, l[j]+l[i])-1
        num=max_c-min_c+1
#        print(str(l[i])+" "+str(l[j])+":"+str(min_c)+" "+str(max_c)+":"+str(num))
        ans += num if num > 0 else 0
print(ans)
