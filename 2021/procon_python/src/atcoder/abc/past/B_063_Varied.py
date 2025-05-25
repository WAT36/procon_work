s=input()
lens=len(s)
sets=len(list(set(s)))
if(lens==sets):
    print("yes")
else:
    print("no")