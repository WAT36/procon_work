fee=[]
for i in range(4):
    fee.append(int(input()))
print(min(fee[0],fee[1]) + min(fee[2],fee[3]))