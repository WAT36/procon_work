n=int(input())
ab_num=0
last_a=0
first_b=0
ba=0
for i in range(n):
    s=input()
    if(s[0]=='B' and s[-1]=='A'):
        ba+=1
    elif(s[0]=='B'):
        first_b+=1
    elif(s[-1]=='A'):
        last_a+=1

    ab_idx=s.find('AB')
    while(ab_idx!=-1):
        ab_num+=1
        ab_idx=s.find('AB',ab_idx+1)

ans=0
if(ba>1):
    ans+=ba-1

if(ba>0):
    if(last_a>0):
        ans+=1
        last_a-=1
    if(first_b>0):
        ans+=1
        first_b-=1
ans+=min(last_a,first_b)
ans+=ab_num
print(ans)