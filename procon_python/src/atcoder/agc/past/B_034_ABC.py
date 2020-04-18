import re
s=input()
ans=0

s=re.sub('BC', 'D', s)

re_ad=re.compile(r'[AD]+')
ad=re.findall(re_ad,s)
#print(s)
#print(ad)
for adi in ad:
    adi_a=0
    for adij in adi:
        if(adij=='A'):
            adi_a+=1
        else:
            ans+=adi_a

print(ans)