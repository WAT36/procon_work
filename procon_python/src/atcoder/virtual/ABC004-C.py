n=int(input())
left=-(-(n%30)//5)+1
if(left==7):
    left=1

trans=0
if(left>1):
    trans=left-1
else:
    trans=6

ans=[]
for i in range(5):
    if(left<=6):
        ans.append(left)
    else:
        left-=6
        ans.append(left)
    left+=1

ind=0
if(n%5!=0):
    ind=n%5
else:
    ind=5

ans.insert(ind, trans)
ans=map(str,ans)
print(''.join(ans))