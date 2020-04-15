s=input()
MAX=99999999999

suits=["S","C","D","H"]
num=["10","J","Q","K","A"]

select_suit=""
min_nextind=MAX
for i in range(len(suits)):
    max_nextj_ind=0
    for j in range(len(num)):
        card_nextind=s.find(suits[i]+num[j])
        if(card_nextind==-1):
            break
        else:
            if(j==0):
                card_nextind+=3
            else:
                card_nextind+=2
            max_nextj_ind=max(max_nextj_ind,card_nextind)
    else:
        if(min_nextind>max_nextj_ind):
            min_nextind=max_nextj_ind
            select_suit=suits[i]

s=s[:min_nextind]
s=s.replace(select_suit+"10", "")
s=s.replace(select_suit+"J", "")
s=s.replace(select_suit+"Q", "")
s=s.replace(select_suit+"K", "")
s=s.replace(select_suit+"A", "")

if(len(s)==0):
    print(0)
else:
    print(s)
