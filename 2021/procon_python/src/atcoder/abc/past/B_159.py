s=input()

def check(s,start,stop):
    a=start
    b=stop
    while(a<=b):
        if(s[a]==s[b]):
            a+=1
            b-=1
        else:
            return False
    return True

if(check(s,0,len(s)-1) and check(s,0,((len(s)-1)//2)-1) and check(s,((len(s)+3)//2)-1,len(s)-1)):
    print("Yes")
else:
    print("No")