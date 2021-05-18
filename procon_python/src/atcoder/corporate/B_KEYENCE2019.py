import sys
s=input()
keyence='keyence'

for i in range(len(s)-1):
    for j in range(len(s)):
        removed_s=s[:i]+s[j+1:]
        if(removed_s==keyence):
            print('YES')
            sys.exit()
else:
    print('NO')
