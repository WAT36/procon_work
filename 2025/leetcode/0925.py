class Solution:
    def isLongPressedName(self, name: str, typed: str) -> bool:
        i=0
        j=0
        icount=0
        jcount=0
        while i<len(name) and j<len(typed):
            if name[i] != typed[j]:
                return False
            
            while i+1<len(name) and name[i]==name[i+1]:
                i+=1
                icount+=1
            i+=1

            while j+1<len(typed) and typed[j]==typed[j+1]:
                j+=1
                jcount+=1
            j+=1

            if icount > jcount:
                return False
            icount=0
            jcount=0
        
        if i<len(name) or j<len(typed):
            return False
        return True
