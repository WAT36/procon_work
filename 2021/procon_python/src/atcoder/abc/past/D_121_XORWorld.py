a,b=map(int,input().split())
one_num=0
if(a%2==0 and b%2==0):
    one_num=(((b-1)-a)+1)//2
    one_num=0 if one_num%2==0 else 1
    print(one_num^b)
elif(a%2==0):
    one_num=((b-a)+1)//2
    one_num=0 if one_num%2==0 else 1
    print(one_num)
elif(b%2==0):
    one_num=(((b-1)-(a+1))+1)//2
    one_num=0 if one_num%2==0 else 1
    print(one_num^a^b)
else:
    one_num=((b-(a+1))+1)//2
    one_num=0 if one_num%2==0 else 1
    print(one_num^a)

