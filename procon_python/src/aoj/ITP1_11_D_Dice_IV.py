import sys

class Dice():
    top=0
    n=1
    e=3
    w=2
    s=4
    bottom=5
    dice=[1,2,3,4,5,6]
    def __init__(self,num):
        self.dice=num

    def roll(self,direction):
        if(direction=="N"):
            self.top,self.bottom,self.n,self.s = self.n,5-self.n,5-self.top,self.top
        elif(direction=="E"):
            self.top,self.bottom,self.e,self.w = self.e,5-self.e,5-self.top,self.top
        elif(direction=="W"):
            self.top,self.bottom,self.e,self.w = self.w,5-self.w,self.top,5-self.top
        elif(direction=="S"):
            self.top,self.bottom,self.n,self.s = self.s,5-self.s,self.top,5-self.top

    def equal(self,another):
        if(self.dice[self.top] != another.dice[another.top]):
            return False
        if(self.dice[self.n] != another.dice[another.n]):
            return False
        if(self.dice[self.e] != another.dice[another.e]):
            return False
        if(self.dice[self.w] != another.dice[another.w]):
            return False
        if(self.dice[self.s] != another.dice[another.s]):
            return False
        if(self.dice[self.bottom] != another.dice[another.bottom]):
            return False

        return True

n=int(input())
dicea=Dice(list(map(int,input().split())))

for i in range(n-1):
    diceb=Dice(list(map(int,input().split())))

    roll_order="NNNNWNNNWNNNENNNENNNWNNNN"
    for j in range(len(roll_order)):
        if(dicea.equal(diceb)):
            print("No")
            sys.exit()
        else:
            diceb.roll(roll_order[j])
print("Yes")