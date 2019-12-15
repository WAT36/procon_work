while(True):
    cards=list(input())
    if(cards[0]=="-"):
        break
    else:
        m=int(input())
        for i in range(m):
            h=int(input())
            withdraw=cards[:h]
            rest=cards[h:]
            cards=rest+withdraw
#            print(cards)
        print(''.join(cards))
