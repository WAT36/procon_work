a=int(input())

k=10
while(True):
    strk=str(k)
    fn=0
    for i in range(len(strk)):
        fn+=int(strk[-1*(i+1)])*(k**i)

#    print(k,fn)
    if(a==fn):
        print(k)
        break
    elif(a<fn):
        print(-1)
        break
    else:
        k+=1
