n=int(input())
alpha=list('abcdefghijklmnopqrstuvwxyz')

def sin(l):
    sinsu=[]
    m=l
    while(m>0):
        if(m%26==0):
            m-=1
            sinsu.append((m%26))
        else:
            sinsu.append((m%26)-1)
        m//=26

    #print(sinsu)
    ans=[]
    for i in range(len(sinsu)):
        ans.append(alpha[sinsu[i]])
    ans=ans[::-1]
#    print(l,end=" ")
    print(''.join(ans))

sin(n)