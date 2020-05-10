s=list(input())


ans=[0 for _ in range(len(s))]

a=0
b=0
r=0
l=0
ind=-1
for i in range(len(s)-1):
    if(s[i]=='R'):
        r+=1

        if(s[i+1]=='L'):
            ind=i
            if(r%2==0):
                a+=r//2
                b+=r//2
            else:
                a+=(r//2)+1
                b+=r//2
    else:
        l+=1

        if(s[i+1]=='R'):
            if(l%2==0):
                a+=l//2
                b+=l//2
            else:
                a+=l//2
                b+=(l//2)+1
            ans[ind]=a
            ans[ind+1]=b
            a=0
            b=0
            l=0
            r=0
            ind=-1
else:
    i+=1
    l+=1

    if(l%2==0):
        a+=l//2
        b+=l//2
    else:
        a+=l//2
        b+=(l//2)+1
    ans[ind]=a
    ans[ind+1]=b

print(*ans)