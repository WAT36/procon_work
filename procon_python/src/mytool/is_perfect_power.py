
#整数aがn乗数であるかを判定する
def is_perfect_power_of_n(a,n):
    nthroot=a**(1/n)
    if(nthroot - int(nthroot) == 0):
        return True
    else:
        return False

#整数aが累乗数であるかを判定する
def is_perfect_power(a):
    n=2
    while(a**(1/n) >= 2):
        nthroot=a**(1/n)
        if(nthroot - int(nthroot) == 0):
            #print(str(a)+" is "+str(int(nthroot)) + "**" + str(n))
            return True
        n+=1

    return False


# for i in range(20):
#     is_perfect_power(i)