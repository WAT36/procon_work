import numpy as np
x,n=map(int,input().split())
p=np.array(list(map(int,input().split())))
p_abs=sorted(list(map(lambda k:abs(k-x),p)))
#print(p_abs)

if(len(p_abs)==0 or p_abs[0]!=0):
    print(x)
else:
    i=1
    while(True):
        if(2*i>=len(p)):
            if(x-i not in p):
                print(x-i)
            else:
                print(x+i)
            break
        elif(p_abs[2*i-1]!=i or p_abs[2*i]!=i):
            if(x-i not in p):
                print(x-i)
            else:
                print(x+i)
            break
        else:
            i+=1