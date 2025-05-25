n,k=map(int,input().split())
st=0
t=[]

for i in range(n):
    t.append(int(input()))
    st+=t[-1]

    if(i>2):
        st-=t[i-3]

    if(i>=2 and st<k):
        print(i+1)
        break
else:
    print(-1)

