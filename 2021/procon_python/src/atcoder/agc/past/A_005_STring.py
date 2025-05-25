x=input()
ans=[]
for i in range(len(x)):
    if(x[i]=='S'):
        ans.append(x[i])
    elif(len(ans)>0 and ans[-1]=='S'):
        ans.pop()
    else:
        ans.append(x[i])
print(len(''.join(ans)))