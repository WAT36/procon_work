class Solution:
    def reorderSpaces(self, text: str) -> str:
        words=[]
        spacecount=text.count(" ")
        for wi in text.split(" "):
            if wi != "":
                words.append(wi)
        spaces=spacecount//(len(words)-1) if len(words)>1 else spacecount
        #print(spacecount,spaces,words)
        ans=""
        for i in range(len(words)):
            ans=ans+words[i]
            if i<len(words)-1:
                ans=ans+(" "*spaces)
        else:
            restspace=spacecount%(len(words)-1) if len(words)>1 else spacecount
            ans=ans+(" "*restspace)
        return ans