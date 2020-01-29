import sys
s=input()
ans=0
i=0
j=len(s)-1
xi=0
yj=0
while(i<j):

    while(i<len(s)-1 and s[i]=='x'):
        i+=1
        xi+=1
#        print(i,xi)

    while(j>0 and s[j]=='x'):
        j-=1
        yj+=1
#        print(j,yj)

#    print(i,xi,j,yj)
    if(s[i]!=s[j]):
        print(-1)
        sys.exit()
    else:
        ans+=abs(xi-yj)
        xi=0
        yj=0
        i+=1
        j-=1

print(ans)