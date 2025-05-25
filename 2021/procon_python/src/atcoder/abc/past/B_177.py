s=input()
t=input()
ans=10**10

for i in range(len(s)-len(t)+1):
    ansi=0
    for j in range(len(t)):
        if(s[i+j]!=t[j]):
            ansi+=1
    ans=min(ans,ansi)

print(ans)