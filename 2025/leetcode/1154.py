class Solution:
    def dayOfYear(self, date: str) -> int:
        days=[31,28,31,30,31,30,31,31,30,31,30,31]
        year=int(date[:4])
        month=int(date[5:7])
        day=int(date[8:])
        if year%4==0:
            if year%100==0:
                if year%400==0:
                    days[1]=29
            else:
                days[1]=29
        #print(month,day)
        return sum(days[:month-1]) + day