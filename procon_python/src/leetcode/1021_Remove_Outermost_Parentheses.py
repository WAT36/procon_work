class Solution:
    def removeOuterParentheses(self, S: str) -> str:
        level=0
        index=[]
        slist=list(S)
        for i in range(len(S)):
            if(S[i]=="("):
                if(level==0):
                    index.append(i)
                level+=1
            else:
                level-=1
                if(level==0):
                    index.append(i)

        for i in range(len(index)):
            slist[index[i]]=''

        return ''.join(slist)

