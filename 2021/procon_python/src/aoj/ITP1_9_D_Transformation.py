s=list(input())
n=int(input())
for i in range(n):
    inst=list(input().split())
    start=int(inst[1])
    end=int(inst[2])
    if(inst[0]=="print"):
        print(''.join(s[start:end+1]))
    elif(inst[0]=="replace"):
        for j in range(len(inst[3])):
            s[start+j]=inst[3][j]
    elif(inst[0]=="reverse"):
        rev=list(reversed(s[start:end+1]))
        for j in range(len(rev)):
            s[start+j]=rev[j]
