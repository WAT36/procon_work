a,b=map(int,input().split())

#a,bの最大公約数
def gcd(a,b):
    if(b==0):
        return a
    else:
        return gcd(b, a%b)

#a,bの最小公倍数
def lcm(a,b):
    return a*b//gcd(a,b)

print(lcm(a,b))