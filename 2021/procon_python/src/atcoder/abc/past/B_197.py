h,w,x,y=map(int,input().split())
s=[]
for i in range(h):
    s.append(list(input()))

ans=1
i=y-2
while(i>=0):
#    print(i)
    if(s[x-1][i]=='.'):
        ans+=1
        i-=1
    else:
        break

i=y
while(i<w):
#    print(i)
    if(s[x-1][i]=='.'):
        ans+=1
        i+=1
    else:
        break

j=x-2
while(j>=0):
#    print(j)
    if(s[j][y-1]=='.'):
        ans+=1
        j-=1
    else:
        break

j=x
while(j<h):
#    print(j)
    if(s[j][y-1]=='.'):
        ans+=1
        j+=1
    else:
        break

print(ans)