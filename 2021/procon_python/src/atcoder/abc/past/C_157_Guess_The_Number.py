import sys
n,m=map(int,input().split())
digit=[-1 for _ in range(n)]
for i in range(m):
    s,c=map(int,input().split())
    if(digit[s-1]==-1):
        digit[s-1]=c
    elif(digit[s-1]!=c):
        print(-1)
        sys.exit()

ans=""

if(n>1 and digit[0]==0):
    print(-1)
    sys.exit()
elif(n>1 and digit[0]==-1):
    digit[0]=1

for i in range(n):
    ans += str(digit[i]) if digit[i]!=-1 else "0"
print(ans)