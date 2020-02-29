x=input()
i=0
while(True):
    if(i>=len(x)):
        print("YES")
        break
    elif(x[i]=='o' or x[i]=='k' or x[i]=='u'):
        i+=1
    elif(x[i:i+2]=='ch'):
        i+=2
    else:
        print("NO")
        break
