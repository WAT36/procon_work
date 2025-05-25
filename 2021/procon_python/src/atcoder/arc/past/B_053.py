s=input()
word={}
for i in range(len(s)):
    wi=word.get(s[i], 0)
    word[s[i]]=wi+1

odd_num=0
even_num=0
for v in word.values():
    if(v%2==0):
        even_num+=v
    else:
        even_num+=v-1
        odd_num+=1

even_num//=2
ans=0
if(odd_num==0):
    ans=2*even_num
else:
    ans=2*(even_num//odd_num)+1

print(ans)