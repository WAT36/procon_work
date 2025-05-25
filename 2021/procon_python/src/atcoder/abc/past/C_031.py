n=int(input())
a=list(map(int,input().split()))
ans=-999999999999999
for i in range(n):
    abi_max=[-999999999999999,-9999999999999999]
    for j in range(n):
        if(j!=i):
            x=min(i,j)
            y=max(i,j)
            aji=a[x:y+1]
            t_sum=sum(aji[0::2])
            a_sum=sum(aji[1::2])
            if(abi_max[1] < a_sum):
                abi_max[1]=a_sum
                abi_max[0]=t_sum
#                print("i:"+str(i)+",j:"+str(j)+","+str(abi_max)+" : "+str(aji[0::2])+"  :  "+str(aji[1::2]))
    if(ans < abi_max[0]):
        ans =abi_max[0]
print(ans)