k,n=map(int,input().split())
a=list(map(int,input().split()))
a.sort()
max_diff=0
for i in range(1,n):
    if(max_diff<a[i]-a[i-1]):
        max_diff=a[i]-a[i-1]
if(max_diff<a[0]+(k-a[-1])):
    max_diff=a[0]+(k-a[-1])
print(k-max_diff)