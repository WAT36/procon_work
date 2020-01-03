x=list(input().split())
stack=[]

for i in range(len(x)):
    if(x[i]=='+'):
        b=stack.pop()
        a=stack.pop()
        stack.append(a+b)
    elif(x[i]=='-'):
        b=stack.pop()
        a=stack.pop()
        stack.append(a-b)
    elif(x[i]=='*'):
        b=stack.pop()
        a=stack.pop()
        stack.append(a*b)
    else:
        stack.append(int(x[i]))

print(stack.pop())


