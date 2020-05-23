award=[100,100,200]
for i in range(3,20):
    award.append(award[-1]+award[-2]+award[-3])
print(award[-1])