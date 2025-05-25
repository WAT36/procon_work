while(True):
    x=list(map(int,input().split()))
    if(x[0]==0 and x[1]==0):
        break
    else:
        x.sort()
        print(str(x[0])+" "+str(x[1]))