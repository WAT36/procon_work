class card:
    def __init__(self,suit,num,input_index):
        self.suit = suit
        self.num = num
        self.input_index = input_index

def partition(p,r):
    c_pivot=cards[r]
    i=p-1
    for j in range(p,r):
        if(cards[j].num<=c_pivot.num):
            i+=1
            cards[i],cards[j]=cards[j],cards[i]
    cards[i+1],cards[r]=cards[r],cards[i+1]
    return i+1

def quicksort(p,r):
    if(p<r):
        q=partition(p,r)
        quicksort(p,q-1)
        quicksort(q+1,r)

n=int(input())
cards=[]
for i in range(n):
    suit,num=input().split()
    cards.append(card(suit,int(num),i))

quicksort(0,n-1)

stableflag=True
for i in range(1,n):
    if(cards[i-1].num == cards[i].num and cards[i-1].input_index > cards[i].input_index):
        stableflag=False
        break
if(stableflag):
    print("Stable")
else:
    print("Not stable")

for ci in cards:
    print(ci.suit,ci.num)
