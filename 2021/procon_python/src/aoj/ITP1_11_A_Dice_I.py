class Dice():
    top=1
    n=2
    e=4
    w=3
    s=5
    dice=[1,2,3,4,5,6]
    def __init__(self,num):
        self.dice=num

    def roll(self,direction):
        if(direction=="N"):
            self.top,self.n,self.s = self.n,7-self.top,self.top
        elif(direction=="E"):
            self.top,self.e,self.w = self.e,7-self.top,self.top
        elif(direction=="W"):
            self.top,self.e,self.w = self.w,self.top,7-self.top
        elif(direction=="S"):
            self.top,self.n,self.s = self.s,self.top,7-self.top


d=list(map(int,input().split()))
dice=Dice(d)
direct=list(input())
for i in range(len(direct)):
    dice.roll(direct[i])

print(dice.dice[dice.top-1])