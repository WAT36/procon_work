s=input()

ans=[]
alpha=list('abcdefghijklmnopqrstuvwxyz')

name=""
atflag=False
for i in range(len(s)):
    if(s[i]=='@'):
        if(atflag and name!=""):
            ans.append(name)
            name=""
        else:
            atflag=True
    elif(s[i] in alpha):
        if(atflag):
            name+=s[i]
    else:
        if(atflag and name!=""):
            ans.append(name)
            name=""
        atflag=False
else:
    if(atflag and name!=""):
        ans.append(name)

ans=list(sorted(list(set(ans))))

for i in range(len(ans)):
    print(ans[i])
