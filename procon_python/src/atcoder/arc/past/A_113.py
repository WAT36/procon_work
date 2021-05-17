k=int(input())
ans=0
for a in range(1,k+1):
    if(a*a*a>k):
        break
    for b in range(a,k+1):
        if(a*b*b>k):
            break
        for c in range(b,k+1):
            if(a*b*c>k):
                break
            elif(a==b and b==c):
                ans+=1
            elif(a==b or b==c or c==a):
                ans+=3
            else:
                ans+=6
print(ans)
