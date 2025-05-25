n=int(input())
s=[]
for i in range(n):
    s.append(int(input()))
if(sum(s)%10!=0):
    print(sum(s))
else:
    s.sort()
    for i in range(n):
        if(s[i]%10!=0):
            print(sum(s)-s[i])
            break
    else:
        print(0)
