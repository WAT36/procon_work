while(True):
    a,b=map(int,input().split())
    if(a==0 and b==0):
        break
    else:
        for i in range(a):
            for j in range(b):
                if(i==0 or j==0 or i==a-1 or j==b-1):
                    print("#",end="")
                else:
                    print(".",end="")
            print()
        print()