s=list(input().split())
ans=[]
for si in s:
    if(si=='Left'):
        ans.append('<')
    elif(si=='Right'):
        ans.append('>')
    else:
        ans.append('A')
print(*ans)
