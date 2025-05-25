n=int(input())
cards=[[False for _ in range(13)] for _ in range(4)]
suits={"S":0,"H":1,"C":2,"D":3}
for i in range(n):
    s,c=input().split()
    cards[suits[s]][int(c)-1] = True

suits_key=list(suits.keys())
for i in range(4):
    for j in range(13):
        if(not cards[i][j]):
            print("{0} {1}".format(suits_key[i],j+1))