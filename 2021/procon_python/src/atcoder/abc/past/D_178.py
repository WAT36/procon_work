s=int(input())
MOD=(10**9)+7

f=[0,0,0,1,1,1]

for i in range(6,s+1):
    fsi=1
    for j in range(3,i-3+1):
        fsi+=f[j]
        fsi%=MOD
#        print("f[{0}]:{1}*f[{2}]:{3}".format(i-j,f[i-j],j,f[j]))
    fsi%=MOD
    f.append(fsi)
#    print(i,f[i])

print(f[s])