s=input()
k=int(input())

ans=[]
for i in range(len(s)-k+1):
    ans.append(s[i:i+k])
print(len(set(ans)))
