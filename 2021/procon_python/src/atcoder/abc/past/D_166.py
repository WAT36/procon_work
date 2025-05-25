x=int(input())

b=0
while(True):
    bi=b**5
    ai=x+bi
#    print(ai,bi,(ai**(1/5))%1.0)
    #X-B^5 は整数を５乗した数か判定
    if(int((ai**(1/5))%1.0) == 0):

        aj=int((ai**(1/5))//1)
#        print(ai,aj,bi,b)
        if((aj**5)==ai):
            print(aj,b)
            break
    b*=-1

    bi=b**5
    ai=x+bi

    if(ai>=0 and int((ai**(1/5))%1.0) == 0):
        aj=int((ai**(1/5))//1)
#        print(ai,aj,bi,b)
        if((aj**5)==ai):
            print(aj,b)
            break
    b*=-1

    b+=1
