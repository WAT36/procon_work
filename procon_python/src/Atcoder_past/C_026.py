n=int(input())
sal_i=[ 1 for x in range(n+1)]
sub_i=[[] for x in range(n+1)]
for i in range(2,n+1):
    boss_i = int(input())
    temp_sub = sub_i[boss_i]
    temp_sub.append(i)
    sub_i[boss_i] = temp_sub
for i in reversed(range(1,n+1)):
    if sub_i[i]:
        sal_sub = [ sal_i[x] for x in sub_i[i]]
        sal = max(sal_sub) + min(sal_sub) + 1
        sal_i[i] = sal
print(sal_i[1])