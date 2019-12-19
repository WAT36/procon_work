class Dice():
    top=1
    n=2
    e=4
    w=3
    s=5
    dice=[1,2,3,4,5,6]

    top_front_right=[[-1,3,5,2,4,-1],[4,-1,1,6,-1,3],[2,6,-1,-1,1,5],
                     [5,1,-1,-1,6,2],[3,-1,6,1,-1,4],[-1,4,2,5,3,-1]]

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
n=int(input())
for i in range(n):
    top,front=map(int,input().split())
    print(d[dice.top_front_right[d.index(top)][d.index(front)]-1])
