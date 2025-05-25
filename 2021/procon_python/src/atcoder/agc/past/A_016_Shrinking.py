s=input()
set_s=list(set(s))
ans=999999999999999
for i in range(len(set_s)):
    si=set_s[i]
    t=list(s)
#    print(t)
    si_ans=0
    while(len(set(t))>1):
        tdash=[]
        for j in range(len(t)-1):
            if(t[j]==si or t[j+1]==si):
                tdash.append(si)
            else:
                tdash.append(t[j])
        t=tdash
#        print(t)
        si_ans+=1
    if(ans > si_ans):
        ans=si_ans
print(ans)