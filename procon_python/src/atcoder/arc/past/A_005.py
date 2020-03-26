n=int(input())
s=input()
s=s[:-1].split()
ans=['TAKAHASHIKUN','Takahashikun','takahashikun']
count=0
for i in range(len(s)):
    if(s[i] in ans):
        count+=1
print(count)