s=input()

if(s=="{}"):
    print("dict")
else:
    depth=0
    for i in range(len(s)):
        if(s[i]=="{"):
            depth+=1
        elif(s[i]=="}"):
            depth-=1
        elif(s[i]==":"):
            if(depth==1):
                print("dict")
                break
        elif(s[i]==","):
            if(depth==1):
                print("set")
                break
    else:
        print("set")