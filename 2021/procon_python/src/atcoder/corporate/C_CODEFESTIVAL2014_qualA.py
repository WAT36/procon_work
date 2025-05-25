a,b=map(int,input().split())

def uru_century(k,l):
    count=0
    for i in range(k,l):
        if(i%400==0):
            count+=1
        elif(i%100==0):
            pass
        elif(i%4==0):
            count+=1
    return count


a_hund=a//100
b_hund=b//100

a_foot=a%100
b_foot=b%100


four_hund=uru_century(1, 401)

if(b-a<=400):
    print(uru_century(a, b+1))
else:
    ans=0
    a_up=400* (-(-a//400))
    ans+=uru_century(a, a_up+1)

    b_down=400*(b//400)
    ans+=uru_century(b_down+1, b+1)

    ans+=four_hund*((b_down-a_up)//400)

    print(ans)
