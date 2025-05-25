import sys
n=int(input())
h=[]

ans=0
mount_start=-1
mount_end=-1
upflag=False
downflag=False
h.append(int(input()))

if(n==1):
    print(1)
    sys.exit()


for i in range(1,n):
    hi=int(input())

    if(h[-1]<hi):
        if(downflag):
            mount_end=i-1
            ansi=mount_end-mount_start+1
            if(ans<ansi):
                ans=ansi
            mount_end=-1
            mount_start=i-1
            upflag=True
            downflag=False
        elif(not upflag):
            upflag=True
            mount_start=i-1
    elif(h[-1]>hi):
        if(upflag):
            upflag=False
            downflag=True
        elif(not downflag):
            downflag=True
            mount_start=i-1
    else:
        mount_end=i-1
        ansi=mount_end-mount_start+1
        if(ans<ansi):
            ans=ansi
        mount_end=-1
        mount_start=-1
        upflag=False
        downflag=False

    h.append(hi)
#    print(hi,mount_start,mount_end,upflag,downflag,ans)
else:
    mount_end=i
    ansi=mount_end-mount_start+1
    if(ans<ansi):
        ans=ansi
#    print(hi,mount_start,mount_end,upflag,downflag,ans)


print(ans)