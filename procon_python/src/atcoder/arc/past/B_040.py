n,r=map(int,input().split())
s=list(input())

goal=0
for i in range(n-1,-1,-1):
    if(s[i]=='.'):
        goal=max(0,i-r+1)
        break

ans=0
prepos=0
nowpos=0
while(nowpos<=goal):

    mostleft_white=-1
    for i in range(n):
        if(s[i]=='.'):
            mostleft_white=i
            break

    if(mostleft_white==-1):
        break

    prepos=nowpos
    nowpos=min(mostleft_white,goal)
    ans+=(nowpos-prepos)

    for i in range(nowpos,nowpos+r):
        if(i<n):
            s[i]='o'
        else:
            break
    ans+=1

#    print(''.join(s),nowpos,ans)


print(ans)
