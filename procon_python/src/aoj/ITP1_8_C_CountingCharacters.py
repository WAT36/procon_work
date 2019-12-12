sentence=""
while(True):
    try:
        sentence+=input().lower()
    except EOFError:
        break

char=ord("a")
while(char<=ord("z")):
    print(chr(char)+" : "+str(sentence.count(chr(char))))
    char+=1