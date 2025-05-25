while(True):
    a,b=map(int,input().split())
    if(a==0 and b==0):
        break
    else:
        for i in range(a):
            for j in range(b):
                if((i+j) % 2 == 0):
                    print("#",end="")
                else:
                    print(".",end="")
            print()
        print()