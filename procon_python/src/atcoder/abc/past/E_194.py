n,m=map(int,input().split())
a=list(map(int,input().split()))

val_ind_dict={}
for i in range(n):
    val_ind=val_ind_dict.get(a[i], [])
    val_ind.append(i)
    val_ind_dict[a[i]]=val_ind

i=0
flag=True
while(flag):
    if(val_ind_dict.get(i,[])==[]):
        print(i)
        break
    else:
        val_ind_list=val_ind_dict[i]
        if(len(val_ind_list)==1):
            if(m-1 < val_ind_list[0] or val_ind_list[0] < n-m):
                print(i)
                break
        else:
            val_ind_list.append(n)
            for j in range(len(val_ind_list)-1):
                if(val_ind_list[j+1]-val_ind_list[j]>=m+1):
                    print(i)
                    flag=False
                    break
    i+=1

