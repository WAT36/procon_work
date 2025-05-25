import sys

n=int(input())
s=list(input())
t=list(input())

s1=s.count('1')
t1=t.count('1')

if(s1<t1 or s1%2 != t1%2):
    print(-1)
    sys.exit()

sone_list=[]
tone_list=[]

for i in range(n):
    if(s[i]=='1'):
        sone_list.append(i)
    if(t[i]=='1'):
        tone_list.append(i)

i=0
j=0
ans=0
while(i<len(sone_list) and j<len(tone_list)):
    if(sone_list[i]<tone_list[j]):
        if(i>=len(sone_list)-1):
            print(-1)
            sys.exit()
        else:
            ans+=sone_list[i+1]-sone_list[i]
            i+=2
    else:
        ans+=sone_list[i]-tone_list[j]
        i+=1
        j+=1

while(i<len(sone_list)):
    ans+=sone_list[i+1]-sone_list[i]
    i+=2

if(j>=len(tone_list)-1):
    print(ans)
else:
    print(-1)