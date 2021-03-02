s=input()
ans=0
prev_si=""
prev_i=len(s)

for i in range(len(s)-3,-1,-1):
    if(s[i]==s[i+1] and s[i+1]!=s[i+2]):
        if(prev_si != s[i]):
            ans+=(len(s)-1)-(i+2)+1-(list(s[i+2:prev_i]).count(s[i]))
        else:
            ans+=(prev_i-1)-(i+2)+1-(list(s[i+2:prev_i]).count(s[i]))
        prev_si=s[i]
        prev_i=i
#    print(i,s[i],ans,prev_i,s[i+2:prev_i],list(s[i+2:prev_i]).count(s[i]))

print(ans)