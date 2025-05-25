n=int(input())
s=[]
s.append(list(input()))
s.append(list(input()))
MOD=1000000007
ans=1
hflag=False
wflag=False
i=0
while(i<n):
    if(s[0][i]==s[1][i]):
        #縦型の時
        if(hflag):
            ans*=2
        elif(wflag):
            ans*=1
        elif((not hflag) and (not wflag)):
            #最初が縦型の時
            ans*=3
#        print(i,ans)
        hflag=True
        wflag=False
        i+=1
    else:
        #横型の時
        if(hflag):
            ans*=2
        elif(wflag):
            ans*=3
        elif((not hflag) and (not wflag)):
            #最初が横型の時
            ans*=6
#        print(i,ans)
        hflag=False
        wflag=True
        i+=2
print(ans%MOD)
