class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        m={}
        for s in strs:
            ikey = ''.join(sorted(s))
            #print(m,ikey)
            if ikey in m:
                mikey= m[ikey]
                mikey.append(s)
                m[ikey] = mikey
            else:
                m[ikey] = [s]
        ans=[]
        for v in m.values():
            ans.append(v)
        return ans