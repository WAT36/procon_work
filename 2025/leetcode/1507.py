class Solution:
    def reformatDate(self, date: str) -> str:
        month=["aa","Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]
        d=date.split(" ")
        return d[2]+"-"+str(month.index(d[1])).zfill(2)+"-"+str(d[0][:-2]).zfill(2)