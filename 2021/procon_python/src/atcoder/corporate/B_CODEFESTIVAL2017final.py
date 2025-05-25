s=input()
a=list(s).count('a')
b=list(s).count('b')
c=list(s).count('c')
if(max(a,b,c)-min(a,b,c)>1):
    print("NO")
else:
    print("YES")

