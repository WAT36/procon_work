import copy
n=int(input())
s=input()
ans=copy.deepcopy(s)
paren=0
for i in range(n):
    if(s[i] == '('):
        paren+=1
    elif(paren <= 0):
        ans = "(" + ans
    else:
        paren-=1

for i in range(paren):
    ans = ans + ")"

print(ans)