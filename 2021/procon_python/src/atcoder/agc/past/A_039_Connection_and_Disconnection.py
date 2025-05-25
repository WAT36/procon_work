s=input()
k=int(input())
t=list(s)
ans=0

if(len(set(list(s)))==1):
    ans=(len(s)*k)//2
elif(s[0] != s[-1]):
    for i in range(len(t)-1):
        if(t[i] == t[i+1]):
            ans+=1
            t[i+1]="*"
    ans*=k
else:
    s_first=s[0]
    first=0
    end=len(s)-1

    while(s[first] == s_first):
        first+=1

    while(s[end] == s_first):
        end-=1

    len_first=first
    len_end=len(s[end+1:])

    rest_s=list(s[first:end+1])
    rest_ans=0
    for i in range(len(rest_s)-1):
        if(rest_s[i] == rest_s[i+1]):
            rest_ans+=1
            rest_s[i+1]="*"

    ans+=len_first//2
    ans+=rest_ans*k
    ans+=((len_first+len_end)//2)*(k-1)
    ans+=len_end//2
print(ans)