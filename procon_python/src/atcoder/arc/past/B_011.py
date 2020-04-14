n=input()
w=list(input().split())
ans=[]

charol={'b':'1','c':'1','t':'3','j':'3','l':'5','v':'5','p':'7','m':'7','n':'9','g':'9',
        'd':'2','w':'2','f':'4','q':'4','s':'6','x':'6','h':'8','k':'8','z':'0','r':'0'}

for i in range(len(w)):
    wi=w[i].lower()
    ans_wi=""
    for j in wi:
        ans_wi+=charol.get(j, "")
#    print(wi,ans_wi)
    if(ans_wi!=""):
        ans.append(ans_wi)
print(*ans)