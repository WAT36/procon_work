class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        if len(intervals) == 0:
            return [newInterval]
        i=0
        start_i=0
        new_start=0
        while i<len(intervals):
            if newInterval[0] < intervals[i][0]:
                start_i=i
                new_start=newInterval[0]
                break
            elif intervals[i][0] <= newInterval[0] and newInterval[0] <= intervals[i][1]:
                start_i=i
                new_start=intervals[i][0]
                break
            i+=1
        else:
            start_i=i
            new_start=newInterval[0]


        i=len(intervals)-1
        end_i=0
        new_end=0
        while 0<=i:
            if intervals[i][1] < newInterval[1]:
                end_i=i
                new_end=newInterval[1]
                break
            elif intervals[i][0] <= newInterval[1] and newInterval[1] <= intervals[i][1]:
                end_i=i
                new_end=intervals[i][1]
                break
            i-=1
        else:
            end_i=i
            new_end=newInterval[1]
        print(start_i,end_i,new_start,new_end)
        ans=[]
        ans.extend(intervals[:start_i])
        ans.append([new_start,new_end])
        ans.extend(intervals[end_i+1:])
        return ans