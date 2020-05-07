n=int(input())
axy=[]

for i in range(n):
    ai=int(input())
    axy.append([])
    for j in range(ai):
        axy[-1].append(list(map(int,input().split())))

ans=0
pat=2**n
#print(axy)
for p in range(pat):
    #i文字目は人iが正直者か日正直者か
    bin_p=list(map(int,bin(p)[2:].zfill(n)))

    flag=False
#    print(bin_p)
    for i in range(n):

        for axyi in axy[i]:
#            print(axyi)
            if(bin_p[i]==1 and bin_p[axyi[0]-1] != axyi[1]):
                flag=True
                break

#             if(bin_p[i]==0 and bin_p[axyi[0]-1] == axyi[1]):
#                 flag=True
#                 break


        if(flag):
            break
    else:
#        print(bin_p,flag)
        ans=max(ans,bin_p.count(1))
print(ans)
