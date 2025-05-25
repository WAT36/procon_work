n=list(map(int,input().split()))
full_num=5**3
sums=[]
for i in range(full_num):
    use_i=[]
    temp_i = i

    for j in range(3):
        use_i.append(temp_i%5)
        temp_i = temp_i//5

    use_i = list(set(use_i))
    if(len(use_i) != 3):
        continue
    else:
        sums.append(n[use_i[0]] + n[use_i[1]] + n[use_i[2]])

sums = list(set(sums))
sums.sort()
print(sums[-3])

