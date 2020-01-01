#正規表現モジュール、あのブログ（対応表の方）に書く
import re
n=int(input())
a=list(map(int,input().split()))
change_num=0
flag=True
while(flag):
    flag=False
    for i in range(n-1):
        if(a[i] > a[i+1]):
            a[i],a[i+1] = a[i+1],a[i]
            change_num+=1
            flag=True
print(re.sub("[\[\]\,]","",str(a)))
print(change_num)
