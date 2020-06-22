n,m=map(int,input().split())
a=sorted(list(map(int,input().split())))[::-1]
b=sorted(list(map(int,input().split())))[::-1]

i=0
j=0
ans=""
while(len(a)>i and len(b)>j):
    if(a[i]>=b[j]):
        i+=1
        j+=1
    else:
        ans="NO"
        break
else:
    if(len(b)>j):
        ans="NO"
    elif(len(a)>i):
        ans="YES"
    else:
        ans="YES"

print(ans)
