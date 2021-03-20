n=int(input())

n_digits=len(str(n))
#print(n_digits)
ans=0
if(n_digits%2==0):
    zenhan=n//(10**(n_digits//2))
#    kohan=n%(10**(n_digits//2))
#    print(zenhan)
    if(n>=(zenhan*(10**(n_digits//2)) +zenhan)):
        ans=zenhan
    else:
        ans=zenhan-1
else:
    ans=10**(n_digits//2) - 1
print(ans)