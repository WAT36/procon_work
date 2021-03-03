k=int(input())
s=input()
t=input()

ans=0


def point(r):
    p=0
    for i in range(1,10):
        p+=(i* 10**(r.count(str(i))))
    return p

com=0
for i in range(1,10):
    si=s[:4]+str(i)
    if(si.count(str(i)) > k):
        continue
    else:
        for j in range(1,10):
            tj=t[:4]+str(j)
            if(si.count(str(i)) + tj.count(str(i)) > k  or
               si.count(str(j)) + tj.count(str(j)) > k):
                continue
            else:
                com+=( (k - (s[:4]+t[:4]).count(str(i))) * (k - (si+t[:4]).count(str(j)) ) )
                if(point(si)>point(tj)):
                    ans+=( (k - (s[:4]+t[:4]).count(str(i))) * (k - (si+t[:4]).count(str(j)) ) )
#                print(si,tj,com,ans,(k - (s[:4]+t[:4]).count(str(i))) , (k - (si+t[:4]).count(str(j)) ))
print(ans/com)