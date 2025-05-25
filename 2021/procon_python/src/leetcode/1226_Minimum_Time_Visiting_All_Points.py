class Solution:
    def minTimeToVisitAllPoints(self, points: list[list[int]]) -> int:
        ans=0
        now=points[0]
        for i in range(1,len(points)):
            next=points[i]
            diff_x=abs(next[0]-now[0])
            diff_y=abs(next[1]-now[1])
            ans+=min(diff_x,diff_y) + abs(diff_y-diff_x)
            now=next
        return ans