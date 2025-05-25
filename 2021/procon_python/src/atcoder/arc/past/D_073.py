n,w=map(int,input().split())

ws=[[] for _ in range(4)]

wi,vi=map(int,input().split())
w1=wi
ws[w1-wi].append(vi)

for i in range(1,n):
    wi,vi=map(int,input().split())
    ws[wi-w1].append(vi)

for i in range(4):
    ws[i]=sorted(ws[i])[::-1]

ans=0
#print(ws)
for i in range(-1,len(ws[0])):
    sum_vi=0
    wi=0

    if(i!=-1):
        sum_vi=sum(ws[0][:i+1])
        wi=w1*(i+1)
    if(wi>w):
#        print("i:{0},wi:{1}".format(i,wi))
        break

    for j in range(-1,len(ws[1])):
        sum_vj=sum_vi
        wj=wi

        if(j!=-1):
            sum_vj=sum_vi+sum(ws[1][:j+1])
            wj=wi+(w1+1)*(j+1)
        if(wj>w):
#            print("i:{0},j:{1},wj:{2}".format(i,j,wj))
            break

        for k in range(-1,len(ws[2])):
            sum_vk=sum_vj
            wk=wj

            if(k!=-1):
                sum_vk=sum_vj+sum(ws[2][:k+1])
                wk=wj+(w1+2)*(k+1)
            if(wk>w):
#                print("i:{0},j:{1},k:{2},wk:{3}".format(i,j,k,wk))
                break

            w_rest=w-wk
            l=w_rest//(w1+3)
            sum_vl=sum_vk
            wl=wk
#            print(sum_vi,sum_vj,sum_vk,wi,wj,wk)
            if(l>len(ws[3])):
                sum_vl+=sum(ws[3])
                wl+=(w1+3)*len(ws[3])
            else:
                sum_vl+=sum(ws[3][:l])
                wl+=(w1+3)*l
#            print("i:{0},j:{1},k:{2},l:{3},wl:{4},w_rest:{5},sum_v:{6}".format(i,j,k,l,wl,w_rest,sum_vl))
            if(ans<sum_vl):
#                print(i,j,k,min(l,len(ws[3])),sum_vl)
                ans=sum_vl
print(ans)