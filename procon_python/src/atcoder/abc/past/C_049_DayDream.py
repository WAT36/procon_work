S=''.join(list(reversed(str(input()))))
words=["maerd","remaerd","esare","resare"]
flag = False
while(True):
    if(len(S) == 0):
        print("YES")
        break
    elif(S[0:len(words[0])] == words[0]):
        S = S[len(words[0]):]
    elif(S[0:len(words[1])] == words[1]):
        S = S[len(words[1]):]
    elif(S[0:len(words[2])] == words[2]):
        S = S[len(words[2]):]
    elif(S[0:len(words[3])] == words[3]):
        S = S[len(words[3]):]
    else:
        print("NO")
        break