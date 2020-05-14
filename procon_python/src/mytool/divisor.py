
#xの約数を列挙する
def divisor(x):
    ans=set([])
    i=1
    while(i*i<=x):
        if(x%i==0):
            ans.add(i)
            ans.add(x//i)
    ans=sorted(list(ans))
    return ans