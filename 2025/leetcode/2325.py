class Solution:
    def decodeMessage(self, key: str, message: str) -> str:
        alpha=list('abcdefghijklmnopqrstuvwxyz')[::-1]
        m={}
        for i in range(len(key)):
            if key[i]!=' ' and key[i] not in m.keys():
                m[key[i]]=alpha.pop()
        ans=""
        for i in range(len(message)):
            if message[i]==' ':
                ans=ans+' '
            else:
                ans=ans+m[message[i]]
        return ans