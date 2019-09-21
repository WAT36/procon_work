n=int(input())
sum99=45*45
forgot=sum99-n
for i in range(1,10):
    if(forgot % i == 0 and forgot//i <= 9):
        print(str(i) + " x " + str(forgot//i))
