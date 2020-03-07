import sys
s=input()
t=input()
cards=list('atcoder')
for i in range(len(s)):
    if(s[i]==t[i]):
        pass
    elif(s[i]=='@' and t[i] in cards):
        pass
    elif(s[i] in cards and t[i]=='@'):
        pass
    else:
        print("You will lose")
        sys.exit()
print("You can win")