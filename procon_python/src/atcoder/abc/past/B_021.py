n=int(input())
abp=list(map(int,input().split()))
k=int(input())
abp.extend(list(map(int,input().split())))
if(len(abp) == len(set(abp))):
    print('YES')
else:
    print('NO')

