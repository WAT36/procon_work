while(True):
    n=input()
    if(n=="0"):
        break
    else:
        ans=0
        for i in range(len(n)):
            ans+=int(n[i])
        print(ans)
