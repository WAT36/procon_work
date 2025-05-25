n=int(input())
a=list(map(int,input().split()))
b=list(map(int,input().split()))

onesum=0
twosum=0
for i in range(n):
    if(a[i]>b[i]):
        onesum+=a[i]-b[i]
    elif(a[i]<b[i]):
        twosum+=(b[i]-a[i])//2

if(onesum<=twosum):
    print("Yes")
else:
    print("No")