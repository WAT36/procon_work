n=int(input())
s=input()
t=input()
i=0
while(i<len(t)):
    if(t[:i+1] in s):
        i+=1
    else:
        break
print(len(s+t[i:]))
