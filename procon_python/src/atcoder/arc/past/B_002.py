y,m,d=map(int,input().split('/'))
day=[31,28,31,30,31,30,31,31,30,31,30,31]

def isuru(y):
    if(y%400==0):
        return True
    elif(y%100==0):
        return False
    elif(y%4==0):
        return True
    else:
        return False


while(y%m!=0 or (y//m)%d!=0):
    if(m==12 and d==31):
        y+=1
        m=1
        d=1
    elif(m==2 and d>=day[m-1] and isuru(y)):
        if(d==day[m-1]):
            d+=1
        else:
            m+=1
            d=1
    elif(d==day[m-1]):
        m+=1
        d=1
    else:
        d+=1

print("{0:02d}/{1:02d}/{2:02d}".format(y,m,d))
