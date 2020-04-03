n,k=map(int,input().split())
r,s,p=map(int,input().split())
t=input()

score=0
scorei=0
myans=[]
myansi=""
for i in range(n):
    if(t[i]=="r"):
        myansi="p"
        scorei=p
    elif(t[i]=="s"):
        myansi="r"
        scorei=r
    else:
        myansi="s"
        scorei=s

    if(i>=k and myansi==myans[i-k]):
        myansi="*"
        scorei=0

    myans.append(myansi)
    score+=scorei
print(score)