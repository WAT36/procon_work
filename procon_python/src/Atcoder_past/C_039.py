S = str(input())
wwi = ""
ans = {"411":"Do","29":"Re","07":"Mi","611":"Fa","49":"So","27":"La","05":"Si"}
for i in range(len(S)):
    if(S[i] == 'W' and S[i+1] == 'W'):
        wwi += str(i)
    if(len(wwi) >= 2):
        break
print(ans[wwi])
