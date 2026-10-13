class Solution:
    def minNumberOfHours(self, initialEnergy: int, initialExperience: int, energy: list[int], experience: list[int]) -> int:
        ans=0
        en=initialEnergy
        ex=initialExperience
        for i in range(len(energy)):
            if en<=energy[i]:
                diff=energy[i]-en+1
                en+=diff
                ans+=diff
            en-=energy[i]
            
            if ex<=experience[i]:
                diff=experience[i]-ex+1
                ex+=diff
                ans+=diff
            ex+=experience[i]
            #print(i,en,ex,ans)
        return ans