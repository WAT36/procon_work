n=int(input())
c=input()
ans=999999999999999999
button=["A","B","X","Y"]
command=[]
for i in range(4):
    for j in range(4):
        command.append(button[i]+button[j])

for i in range(len(command)):
    for j in range(len(command)):
        ci=c.replace(command[i],"L")
        cj=ci.replace(command[j],"R")
        if(ans>len(cj)):
            ans=len(cj)
print(ans)