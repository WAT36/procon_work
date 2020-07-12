n=int(input())
x=input()
ans=[]

bin_n=bin(n)[2:]
n_zero=bin_n.count('0')
n_one=bin_n.count('1')


def calc_popcount(z):
    bin_z=bin(z)[2:]
    ans=bin_z.count('1')
    return ans

for i in range(n):
    xi=x[:i]+ ('0' if x[i]=='1' else '1') + x[i+1:]
    xi=int(xi,2)
#    print(xi,x[:i]+ ('0' if x[i]=='1' else '1') + x[i+1:])
    ans_xi=0

    while(xi>0):
        xi=xi%calc_popcount(xi)
        ans_xi+=1
    ans.append(ans_xi)

for i in range(len(ans)):
    print(ans[i])

