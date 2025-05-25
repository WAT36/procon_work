n=int(input())
nbin=bin(n)
ans=[]
for i in range(4):
    bi=nbin[-1 * (i+1)]
    if(bi=="b"):
        break
    elif(bi=="1"):
        ans.append(2 ** i)
print(len(ans))
for i in range(len(ans)):
    print(ans[i])