s=input()
a,b,c,d=map(int,input().split())
if(a!=0):
    print(s[:a]+'"'+s[a:b]+'"'+s[b:c]+'"'+s[c:d]+'"'+s[d:])
else:
    print('"'+s[:b]+'"'+s[b:c]+'"'+s[c:d]+'"'+s[d:])