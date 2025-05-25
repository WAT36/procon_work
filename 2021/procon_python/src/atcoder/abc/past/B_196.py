x=input()
ans=""
for i in range(len(x)):
    if(x[i]=='.'):
        break
    else:
        ans+=x[i]
print(ans)