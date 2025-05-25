import bisect
n,a,b,c=map(int,input().split())
l=[int(input()) for x in range(n)]
l.sort()
total=4**n
ans=999999999
for i in range(total):
    fora=[]
    forb=[]
    forc=[]
    nonused=[]
    temp_i = i
    for j in range(n):
        temp=temp_i%4
        if(temp==0):
            fora.append(l[j])
        elif(temp==1):
            forb.append(l[j])
        elif(temp==2):
            forc.append(l[j])
        else:
            nonused.append(l[j])
        temp_i = temp_i // 4
    if(len(fora)==0 or len(forb)==0 or len(forc)==0):
        continue
    else:
        mp=0
        mp+=10*(len(fora)-1)
        len_fora=sum(fora)
        mp+=abs(a-len_fora)

        mp+=10*(len(forb)-1)
        len_forb=sum(forb)
        mp+=abs(b-len_forb)

        mp+=10*(len(forc)-1)
        len_forc=sum(forc)
        mp+=abs(c-len_forc)

        if(ans > mp):
            ans = mp
print(ans)