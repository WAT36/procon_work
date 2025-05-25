import numpy as np
x=int(input())

xi=set([0])
i=1
while(True):
    list_xi=np.array(list(xi))
    ans_xi=[]
    for xj in list_xi:
        ans_xi.append(xj-i)
        ans_xi.append(xj)
        ans_xi.append(xj+i)
    xi=set(ans_xi)
    print(i,xi)
    if(x in xi):
        print(i)
        break
    else:
        i+=1