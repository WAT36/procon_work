n,k=map(int,input().split())
s=input()

nums=[]

if(s[0]=='0'):
    nums.append(0)

num=s[0]
numi=0
for i in range(n):
    if(s[i]==num):
        numi+=1
    else:
        nums.append(numi)
        numi=1
        num=s[i]
else:
    nums.append(numi)

if(s[-1]=='1'):
    nums.append(0)

#print(nums)

ans=0
zero_num=len(nums)//2
if(zero_num<=k):
    print(sum(nums))
else:
    l=2*k
    sumi=sum(nums[:l+1])
    ans=sumi
    i=0
    while(l+2<len(nums)):
        sumi+=(nums[l+1]+nums[l+2])
        l+=2
        sumi-=(nums[i]+nums[i+1])
        i+=2
        ans=max(ans,sumi)
#    print(nums[-2*k:])
    ans=max(ans,sum(nums[-2*k:]))
    print(ans)