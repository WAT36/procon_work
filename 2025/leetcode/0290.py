class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        sarr=s.split(' ')
        if len(pattern) != len(sarr):
            return False
        m={}
        for i in range(len(pattern)):
            if pattern[i] not in m:
                m[pattern[i]] = sarr[i]
            elif m[pattern[i]] != sarr[i]:
                return False
            #print(pattern[i],m)
        else:
            if len(m.values()) != len(list(set(m.values()))):
                return False
        return True
