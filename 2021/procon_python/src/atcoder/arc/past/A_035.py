s=input()
a=0
b=len(s)-1
while(a<=b):
    if(s[a]=='*' or s[b]=='*'):
        pass
    elif(s[a]!=s[b]):
        print("NO")
        break

    a+=1
    b-=1
else:
    print("YES")