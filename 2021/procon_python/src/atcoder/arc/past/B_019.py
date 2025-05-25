a=input()
len_a=len(a)
a_former=""
a_latter=""
ans=0
flag=False
if(len_a%2==0):
    a_former=a[:(len_a//2)]
    a_latter=a[(len_a//2):]
    a_latter=a_latter[::-1]
else:
    a_former=a[:(len_a-1)//2]
    a_latter=a[(len_a+1)//2:]
    a_latter=a_latter[::-1]
    flag=True

#print(a_former)
#print(a_latter)

diff=0
for i in range(len(a_former)):
    if(a_former[i]!=a_latter[i]):
        diff+=1

if(diff==1):
    ans=25*2*(len(a_former)-1) + (24*2)
else:
    ans=25*2*(len(a_former))

if(flag and diff!=0):
    ans+=25
print(ans)